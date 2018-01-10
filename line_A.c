#include<graphics.h>
#include<stdlib.h>
#include<stdio.h>
#include<conio.h>

int main(void)
{
	int gdriver=DETECT,gmode;
	intgraph(&gdriver,&gmode,"c:\\tc\\bgi");
	line(0,0,20,20);
	getch();
	closegraph();
	return 0;
}