//CTPClient.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>


void main()
{
    int clientSocket;
    struct sockaddr_in serverAddr;
    char buffer[1024];
    
    clientSocket = socket(PF_INET, SOCK_STREAM, 0);

    



}