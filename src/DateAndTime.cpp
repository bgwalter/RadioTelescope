/*
	DateAndTime.cpp
	2015 October 21
	Brendon Walter

	Methods for the date and time classes found in DateAndTime.h

	TODO: Figure out how to get real input for months and days in the 
		GregorianDate class
*/

#include "DateAndTime.h"


/* Methods for the GregorianDate class */

GregorianDate::GregorianDate() { year = 0; month = 0; day = 0; }

GregorianDate::GregorianDate(int y, int m, int d) {
	setDate(y, m, d);
}

bool GregorianDate::setDay(int d) {
	day = d;
	return 1;
}

bool GregorianDate::setMonth(int m) {
	month = m;
	return 1;
}

bool GregorianDate::setYear(int y) {
	year = y;
	return 1;
}

bool GregorianDate::setDate(int y, int m, int d) {
	setYear(y);
	setMonth(m);
	setDay(d);
	return 1;
}

int GregorianDate::getDay()   { return day; }
int GregorianDate::getMonth() { return month; }
int GregorianDate::getYear()  { return year; }
std::string GregorianDate::getDate() { 
	std::stringstream date;
	date << year << "/" << month << "/" << day;
	return date.str();
}

// doesn't work...
float GregorianDate::getJulianDay() {
	return day - 32075 + 1461*(year + 4800 + (month - 14)/12)/4 + 
		   367*(month - 2 - (month - 14)/12*12) / 2/12 - 
		   3*((year + 4900 + (month - 14)/12)/100)/4;
}