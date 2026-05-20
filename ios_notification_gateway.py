from security_logging_service import logger

def send_ios_notification(message):

    logger.info(
        f"iOS push notification sent: {message}"
    )

    return {
        "notification_sent": True
    }
