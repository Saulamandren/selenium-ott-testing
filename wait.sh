#!/bin/bash

echo "Waiting for Selenium Hub UI..."

until curl -s http://localhost:4444/ui > /dev/null; do
  echo "Selenium UI not ready yet..."
  sleep 3
done

echo "Selenium Hub UI is ready!"
