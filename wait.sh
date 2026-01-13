#!/bin/bash

echo "Waiting for Selenium Hub to be ready..."

until curl -s http://localhost:4444/wd/hub/status | grep '"ready":true'; do
  echo "Selenium is not ready yet..."
  sleep 2
done

echo "Selenium Hub is ready!"
