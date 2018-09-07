<?php
  $log_file_name = '7RaZUP6RCVfEdkmxEH6y.log'; // Change to the log file name

  date_default_timezone_set('America/New_York');
  $message = date("YmdHis") . " " . date("Y-m-d H:i:s") . " "; 
  $message .= $_POST['message']; // incoming message
  $message = str_replace("\r\n", ' ', $message);
  $message = str_replace("\n", ' ', $message);
  $message = str_replace("\r", ' ', $message);
  $message .= "\n";
  file_put_contents($log_file_name, $message, FILE_APPEND);
  header('Location: /success.html'); // redirect back to the main site
?>