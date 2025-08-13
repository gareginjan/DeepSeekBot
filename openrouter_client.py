#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenRouter AI client for DeepSeek R1 integration
"""

import aiohttp
import asyncio
import json
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class OpenRouterClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "deepseek/deepseek-r1"
        self.session = None
        
    async def _get_session(self):
        """Get or create aiohttp session"""
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=30)
            self.session = aiohttp.ClientSession(timeout=timeout)
        return self.session
    
    async def generate_response(self, messages: List[Dict], max_tokens: int = 600) -> Optional[str]:
        """Generate response using OpenRouter API"""
        try:
            session = await self._get_session()
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/telegram-bot-sanych",
                "X-Title": "Telegram Bot Sanych"
            }
            
            payload = {
                "model": self.model,
                "messages": messages,
                "max_tokens": min(max_tokens, 600),  # Limit to 600 tokens to fit budget
                "temperature": 0.7,
                "top_p": 0.9,
                "frequency_penalty": 0.1,
                "presence_penalty": 0.1,
                "stream": False
            }
            
            logger.info(f"Sending request to OpenRouter with {len(messages)} messages")
            
            async with session.post(f"{self.base_url}/chat/completions", 
                                  headers=headers, 
                                  json=payload) as response:
                
                if response.status == 200:
                    data = await response.json()
                    
                    if "choices" in data and len(data["choices"]) > 0:
                        content = data["choices"][0]["message"]["content"]
                        logger.info(f"Generated response: {len(content)} characters")
                        return content.strip()
                    else:
                        logger.error(f"No choices in response: {data}")
                        return None
                        
                else:
                    error_text = await response.text()
                    logger.error(f"OpenRouter API error {response.status}: {error_text}")
                    return None
                    
        except asyncio.TimeoutError:
            logger.error("Timeout while calling OpenRouter API")
            return None
        except aiohttp.ClientError as e:
            logger.error(f"HTTP client error: {e}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error calling OpenRouter API: {e}")
            return None
    
    async def close(self):
        """Close the aiohttp session"""
        if self.session and not self.session.closed:
            await self.session.close()
    
    def __del__(self):
        """Cleanup on destruction"""
        if self.session and not self.session.closed:
            try:
                asyncio.get_event_loop().run_until_complete(self.close())
            except:
                pass
