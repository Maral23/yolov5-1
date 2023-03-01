# SEND AN EMAIL ALERT WITH TIMESTAMP (AND TYPE OF PPE) DETECTED
import smtplib
from smtplib import SMTPException
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)

def alert_notification(now,ppe_class):
    ppe_class = round(ppe_class.item())
    date = now.strftime("%x")
    time = now.strftime("%H:%M:%S")
    manager = "Joshua Smith"
    location = 'Factory 1'
    camera = 1
    sender = 'mkorpeyeva@gmail.com'
    receiver = ["mkorpeyeva@gmail.com"]

    #text to be sent
    subject = 'Detected Incompliance'
    general = 'Please take note that incompliance was detected at: '
    date_detected = f'Detected Date :  {date}'
    time_detected = f'Detected Time:  {time}'
    ppe_detected = f'Detected PPE incompliance type: {ppe_class}'
    location_detected = f'Detected Location: {location}'
    camera_detected = f'Detected from Camera # {camera}'
    manager_detected = f'Manager in charge: {manager}'
        
    message = 'Subject: {}\n\n{}\n\n{}\n{}\n{}\n{}\n{}\n{}'.format(subject, general,date_detected, time_detected, ppe_detected,location_detected,camera_detected,manager_detected)
    try:
        session = smtplib.SMTP('smtp.gmail.com',587)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(sender,'yvunzjvwzgmphicj')
        session.sendmail(sender,receiver,message)
        session.quit()
    except SMTPException:
        print('Error occured - Could NOT send email')
       
    # sender = 'mkorpeyeva@gmail.com'
    # receiver = ["mkorpeyeva@gmail.com"]
    # subject = 'Detected Incompliance'
    # text = f'Please take note that incompliance was detected at:  {time_now}'
    # message = 'Subject: {}\n\n{}'.format(subject, text)
    # try:
    #     session = smtplib.SMTP('smtp.gmail.com',587)
    #     session.ehlo()
    #     session.starttls()
    #     session.ehlo()
    #     session.login(sender,'yvunzjvwzgmphicj')
    #     session.sendmail(sender,receiver,message)
    #     session.quit()
    # except SMTPException:
    #     print('Error occured - Could NOT send email')

