#include "CoordinateSystems.h"
#include "AltAz.h"
#include "RADec.h"
#include "LatLon.h"
#include "DateAndTime.h"

using namespace std;

int main(void) {
	RA ra;
	ra.setRA(12, 20, 2);
	cout << ra.getRA() <<endl;
	cout << ra.toHours() <<endl;
	cout << ra.toDegrees() <<endl;
	
	cout<<endl;

	Dec dec;
	dec.setDec(89, 10, 20);
	cout << dec.getDec() <<endl;
	cout << dec.toDegrees() <<endl;
	
	cout<<endl;

	Alt alt;
	alt.setAlt(20);
	cout << alt.getAlt() <<endl;
	
	cout<<endl;

	Az az;
	az.setAz(30);
	cout << az.getAz() <<endl;
	
	cout<<endl;

	Lat lat;
	lat.setLat(10, 'S', 0, 0);
	cout << lat.getLat() <<endl;
	cout << lat.toDegrees() <<endl;
	
	cout<<endl;

	Lon lon;
	lon.setLon(20, 'E', 0, 0);
	cout << lon.getLon() <<endl;
	cout << lon.toDegrees() <<endl;

	GregorianDate gd;
	gd.setDate(2015, 10, 21);
	cout << gd.getDate() <<endl;
	cout << gd.getJulianDay() <<endl;
}
