# Overview

This is a Telegram bot named "Саныч" that integrates with DeepSeek R1 AI model through OpenRouter API. The bot provides intelligent conversational responses in Russian, maintaining context memory for natural dialogue flow. It responds to mentions of "Саныч" in group chats and replies to messages directed at it, using AI to generate contextually relevant responses.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Components

**Modular Architecture**: The application follows a clean separation of concerns with dedicated modules for different functionalities:
- `TelegramBot` class serves as the main orchestrator
- `OpenRouterClient` handles AI API interactions  
- `MessageMemory` manages conversation context
- `BotConfig` centralizes configuration management

**Event-Driven Design**: Built on the python-telegram-bot framework using async/await patterns for handling Telegram updates. The bot processes incoming messages through event handlers that trigger AI responses when specific conditions are met.

**Context Management**: Implements a sliding window memory system that maintains the last 200 messages per chat using collections.deque for efficient memory management. This enables contextual conversations while preventing memory bloat.

**Error Handling and Resilience**: Comprehensive error handling throughout all components with automatic retry mechanisms and graceful degradation. The keep-alive system prevents service interruption on hosting platforms.

**AI Integration Pattern**: Uses OpenRouter as a proxy service to access DeepSeek R1, allowing for easy model switching and rate limiting management. The client implements proper authentication headers and request formatting for the OpenAI-compatible API.

## Message Processing Flow

The bot processes messages through a pipeline:
1. Message filtering (checks for "Саныч" mentions or replies)
2. Context retrieval from memory
3. AI prompt construction with conversation history
4. Response generation via OpenRouter
5. Memory update with new messages

## Scalability Considerations

Thread-safe message memory with locking mechanisms to handle concurrent chat operations. The deque-based storage automatically manages memory limits per chat, preventing unbounded growth.

# External Dependencies

**Telegram Bot API**: Primary interface for receiving and sending messages through the python-telegram-bot library. Handles webhook/polling modes and provides async message handling capabilities.

**OpenRouter AI Service**: Serves as the AI inference provider, offering access to DeepSeek R1 model through OpenAI-compatible REST API. Requires API key authentication and credit balance management.

**HTTP Keep-Alive Service**: Simple HTTP server for health checks, particularly important for Replit hosting environment to prevent service sleep.

**Runtime Dependencies**: 
- `aiohttp` for async HTTP client operations
- `python-telegram-bot` for Telegram API integration
- Standard library modules for threading, logging, and data structures

**Environment Configuration**: Requires `TELEGRAM_BOT_TOKEN` and `OPENROUTER_API_KEY` environment variables for authentication. Optional `REPL_URL` for keep-alive functionality on Replit platform.