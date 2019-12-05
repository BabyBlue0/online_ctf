#include<stdio.h>

int main( void ){
	FILE *fp;
	int c;

	FILE *ofp;

	if( (ofp = fopen("str.txt", "w")) != NULL && 
		(fp = fopen("core","r") ) != NULL ) {
		while( (c = fgetc(fp) ) != EOF ) {
			if( c != '\0') c ^= 1;
			fprintf(ofp,"%c", c );
		}
		fclose( fp );
		fclose( ofp );
	}
	return 0;
}
