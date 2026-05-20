TOP_ALERT_QUERY = '''
SELECT
    severity,
    COUNT(*) AS total_alerts
FROM security_alerts
GROUP BY severity
'''
