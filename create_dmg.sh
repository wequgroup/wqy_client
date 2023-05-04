#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 path/to/your/file"
    exit 1
fi

file_path="$1"
volume_name="app"
dmg_size="100M"

hdiutil create -size $dmg_size -fs HFS+ -volname $volume_name "${volume_name}.dmg"
mount_info=$(hdiutil attach "${volume_name}.dmg")
device_path=$(echo "$mount_info" | grep -o "/dev/disk[0-9]*s[0-9]*")
mount_point=$(echo "$mount_info" | grep -o "/Volumes/$volume_name")
cp -R "$file_path" "$mount_point/"
hdiutil detach "$device_path"
hdiutil convert "${volume_name}.dmg" -format UDZO -o "compressed_${volume_name}.dmg"
rm "${volume_name}.dmg"
echo "Compressed DMG file created: compressed_${volume_name}.dmg"
