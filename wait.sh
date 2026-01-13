#!/bin/bash
# Menentukan bahwa file ini adalah script bash

# Loop sampai Selenium Hub bisa diakses di port 4444
until $(curl --output /dev/null --silent --head --fail http://localhost:4444); do
    # Menampilkan pesan bahwa Selenium Hub masih belum siap
    echo "waiting for selenium hub being started"

    # Menunggu 1 detik sebelum mencoba lagi
    sleep 1
done
