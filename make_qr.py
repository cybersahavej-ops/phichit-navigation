"""หลังอัปโหลด index.html และ map.png ขึ้นเว็บ ให้รัน: python make_qr.py https://your-public-website.example/"""
import sys
import qrcode
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
    raise SystemExit('วิธีใช้: python make_qr.py https://ลิงก์เว็บไซต์จริง/')
qrcode.make(sys.argv[1]).save('qr_code.png')
print('สร้าง qr_code.png สำเร็จ:',sys.argv[1])
