#include <time.h>
#include <string>
#include <sstream>

class GregorianDate {
  private:
	int day, month, year;

  public:
	GregorianDate();
	GregorianDate(int, int, int);

	bool setDay(int);
	bool setMonth(int);
	bool setYear(int);
	bool setDate(int, int, int);

	int getDay();
	int getMonth();
	int getYear();
	std::string getDate();

	float getJulianDay();
};