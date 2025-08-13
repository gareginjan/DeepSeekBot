#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Message memory management for maintaining chat context
"""

import logging
from collections import deque, defaultdict
from typing import Dict, List, Any
import threading

logger = logging.getLogger(__name__)

class MessageMemory:
    def __init__(self, max_messages_per_chat: int = 200):
        self.max_messages_per_chat = max_messages_per_chat
        self._chat_memories = defaultdict(lambda: deque(maxlen=self.max_messages_per_chat))
        self._lock = threading.Lock()
        
        logger.info(f"MessageMemory initialized with max {max_messages_per_chat} messages per chat")
    
    def add_message(self, chat_id: int, message_data: Dict[str, Any]):
        """Add a message to chat memory"""
        try:
            with self._lock:
                self._chat_memories[chat_id].append(message_data)
                
            logger.debug(f"Added message to chat {chat_id}, total messages: {len(self._chat_memories[chat_id])}")
            
        except Exception as e:
            logger.error(f"Error adding message to memory: {e}")
    
    def get_chat_messages(self, chat_id: int) -> List[Dict[str, Any]]:
        """Get all messages for a specific chat"""
        try:
            with self._lock:
                messages = list(self._chat_memories[chat_id])
            
            logger.debug(f"Retrieved {len(messages)} messages for chat {chat_id}")
            return messages
            
        except Exception as e:
            logger.error(f"Error retrieving messages for chat {chat_id}: {e}")
            return []
    
    def get_recent_messages(self, chat_id: int, count: int = 10) -> List[Dict[str, Any]]:
        """Get recent messages for a specific chat"""
        try:
            with self._lock:
                messages = list(self._chat_memories[chat_id])
            
            recent = messages[-count:] if len(messages) > count else messages
            logger.debug(f"Retrieved {len(recent)} recent messages for chat {chat_id}")
            return recent
            
        except Exception as e:
            logger.error(f"Error retrieving recent messages for chat {chat_id}: {e}")
            return []
    
    def clear_chat_memory(self, chat_id: int):
        """Clear all messages for a specific chat"""
        try:
            with self._lock:
                if chat_id in self._chat_memories:
                    self._chat_memories[chat_id].clear()
            
            logger.info(f"Cleared memory for chat {chat_id}")
            
        except Exception as e:
            logger.error(f"Error clearing memory for chat {chat_id}: {e}")
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory usage statistics"""
        try:
            with self._lock:
                stats = {
                    'total_chats': len(self._chat_memories),
                    'total_messages': sum(len(messages) for messages in self._chat_memories.values()),
                    'chat_details': {
                        chat_id: len(messages) 
                        for chat_id, messages in self._chat_memories.items()
                    }
                }
            
            logger.debug(f"Memory stats: {stats['total_chats']} chats, {stats['total_messages']} total messages")
            return stats
            
        except Exception as e:
            logger.error(f"Error getting memory stats: {e}")
            return {'total_chats': 0, 'total_messages': 0, 'chat_details': {}}
    
    def cleanup_old_chats(self, keep_recent_chats: int = 100):
        """Remove memory for oldest chats if too many chats are stored"""
        try:
            with self._lock:
                if len(self._chat_memories) > keep_recent_chats:
                    # Sort by number of messages (keep more active chats)
                    sorted_chats = sorted(
                        self._chat_memories.items(),
                        key=lambda x: len(x[1]),
                        reverse=True
                    )
                    
                    # Keep only the most active chats
                    chats_to_remove = sorted_chats[keep_recent_chats:]
                    
                    for chat_id, _ in chats_to_remove:
                        del self._chat_memories[chat_id]
                    
                    logger.info(f"Cleaned up {len(chats_to_remove)} old chats")
            
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
