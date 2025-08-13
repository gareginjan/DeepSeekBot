#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot configuration with environment variables
"""

import os
import logging

logger = logging.getLogger(__name__)

class BotConfig:
    def __init__(self):
        self.telegram_bot_token = self._get_env_var('TELEGRAM_BOT_TOKEN')
        self.openrouter_api_key = self._get_env_var('OPENROUTER_API_KEY')
        
        # OpenRouter configuration
        self.openrouter_base_url = "https://openrouter.ai/api/v1"
        self.model_name = "deepseek/deepseek-r1"
        
        # Bot configuration
        self.max_context_messages = 200
        self.max_response_length = 4000  # Telegram message limit is ~4096 chars
        
        logger.info("Bot configuration loaded successfully")

    def _get_env_var(self, var_name: str, default: str = None) -> str:
        """Get environment variable with error handling"""
        value = os.getenv(var_name, default)
        if not value:
            logger.error(f"Environment variable {var_name} is not set!")
            raise ValueError(f"Environment variable {var_name} is required!")
        return value

    def get_openrouter_headers(self) -> dict:
        """Get headers for OpenRouter API requests"""
        return {
            "Authorization": f"Bearer {self.openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/telegram-bot",
            "X-Title": "Telegram Bot Sanych"
        }
