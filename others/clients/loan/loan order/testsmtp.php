<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'testsmtp/PHPMailer-master/src/Exception.php';
require'testsmtp/PHPMailer-master/src/PHPMailer.php';
require 'testsmtp/PHPMailer-master/src/SMTP.php';

// Настройки сервера на примере Яндекс почты
$mail = new PHPMailer;
$mail->isSMTP();                                     
$mail->Host         = 'srv-plesk53.ps.kz';
$mail->Port         = 587;
$mail->SMTPAuth     = true;
$mail->Username     = 'test@main.kernelx.ru'; // Если почта для домена, то логин это полный адрес почты
$mail->Password     = 'Nimeria_1227';
$mail->SMTPSecure   = 'TLS';


// Авторизация
$mail->CharSet = 'UTF-8';
$mail->From = 'test@main.kernelx.ru';
$mail->FromName = 'test@main.kernelx.ru';
$mailadr = $_POST['email'];
$mail->addAddress($mailadr);


// Контент  
$select_urlico = $_POST['select_urlico'];
$company_name = $_POST['company_name'];
$loan_sum = $_POST['loan_sum'];
$times = $_POST['times'];
$select_zalog = $_POST['select_zalog'];
$select_target = $_POST['select_target'];
$select_address	 = $_POST['select_address'];
$phone = $_POST['phone'];
$email = $_POST['email'];
#$mail->isHTML(true);                    
$mail->Subject = "Заявка на кредит";

$mail->Body ="Форма юр лица: $select_urlico \n 
Наименование компании : $company_name   \n 
Сумма кредита в тенге:$loan_sum   \n 
Срок кредита в месяцах: $times  \n 
Залоговое имущество:$select_zalog  \n 
Цель кредита: $select_target   \n 
Район регистрации юр лица: $select_address  \n 
Телефон: $phone  \n 
Email:$email \n ";
#$email = $_POST['email']; // this is the sender's Email address


// Отправка
if(!$mail->send()) {
    echo 'Сообщение не может быть отправлено.';
    echo 'Ошибка: ' . $mail->ErrorInfo;
    exit;
}
else{
    echo 'Сообщение отправлено по адресу. ';
	echo $mailadr;
}
?>
