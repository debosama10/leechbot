if [[ -n $RCLONE_CONFIG ]]; then
 echo "rclone config detected"
 echo -e "$RCLONE_CONFIG" > /app/rclone.conf
fi
python3 -m leechbot
