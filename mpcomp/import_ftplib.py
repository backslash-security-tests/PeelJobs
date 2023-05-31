from ftplib import FTP

def test_vuln():
    ftp = FTP('ftp.debian.org')
    ftp.login()

    ftp.cwd('debian')
    ftp.retrlines('LIST')

    ftp.quit()
