#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keep-alive mechanism to prevent the bot from sleeping
"""

import time
import threading
import logging
import requests
from urllib.parse import urlparse
import os

logger = logging.getLogger(__name__)

def keep_alive_thread():
    """Keep alive thread function"""
    logger.info("Keep-alive thread started")
    
    # Get current URL if running on Replit
    replit_url = os.getenv('REPL_URL')
    
    while True:
        try:
            # Sleep for 5 minutes
            time.sleep(300)  # 300 seconds = 5 minutes
            
            # Send a simple HTTP request to keep the service alive
            if replit_url:
                try:
                    response = requests.get(f"{replit_url}/health", timeout=10)
                    logger.debug(f"Keep-alive ping status: {response.status_code}")
                except requests.RequestException as e:
                    logger.debug(f"Keep-alive ping failed (this is normal): {e}")
            
            # Log heartbeat
            logger.info("Keep-alive heartbeat")
            
        except Exception as e:
            logger.error(f"Error in keep-alive thread: {e}")
            time.sleep(60)  # Wait 1 minute before retrying

def start_keep_alive_server():
    """Start a simple HTTP server for health checks"""
    try:
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        import socketserver
        
        class HealthHandler(SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/health':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'OK')
                else:
                    self.send_response(404)
                    self.end_headers()
            
            def log_message(self, format, *args):
                # Suppress HTTP server logs
                pass
        
        # Try to bind to port 5000 (frontend port)
        try:
            httpd = HTTPServer(('0.0.0.0', 5000), HealthHandler)
            server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
            server_thread.start()
            logger.info("Health check server started on port 5000")
        except OSError:
            # Port might be in use, that's okay
            logger.debug("Could not start health server on port 5000 (port in use)")
            
    except ImportError:
        logger.debug("HTTP server not available, skipping health check server")
    except Exception as e:
        logger.error(f"Error starting health check server: {e}")

# Start the health check server when module is imported
start_keep_alive_server()
