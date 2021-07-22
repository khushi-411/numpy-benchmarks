// Mentor: Matti Picus
// Reference: http://initialconditions.org/codes/1

/* 
 * TODO:
 *     1. Operator Overloading
 *     2. Convert to Mordern C++ 
 *     3. 
 */     

#include <iostream>
#include <vector>
#include <math.h>
#include <numeric>

typedef double real;

using namespace std;

class Star {
	public:
		real m;
		vector <real> r;
		vector <real> v;
		vector <real> a, a0;


		// Default Constructor
		Star() {
			r.assign(3, 0);
			v.assign(3, 0);
			a.assign(3, 0);
			a0.assign(3, 0);
		}

		// Detailed constructor
		Star(real mass, vector <real> position, vector <real> velocity) {
			m = mass;
			r = position;
			v = velocity;
		}
		
		// https://stackoverflow.com/questions/21995521/what-is-friend-ostream/21995556
		// https://stackoverflow.com/questions/236801/should-operator-be-implemented-as-a-friend-or-as-a-member-function
		friend ostream &operator << (ostream &so, const Star &si) {
			so << si.m << " " << si.r[0] << " " << si.r[1] << " " << si.r[2] << " "
				<< si.v[0] << " " << si.v[1] << " " << si.v[2] << endl;
			return so;
		}
};

class Cluster : public Star {
	protected:
	public:
		vector <Star> s;
		cluster() : Star() {}

		void acceleration() {
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++) {
				si -> assign(3, 0);
			// For each start
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++) {
				vector <real> rij(3);
				real init = 0.0;
				// For each remaining star
				for (vector<Star>::iterator sj = s.begin(); si != s.end(); si++) {
					if(si != sj) {
						// Distance between two stars
						rij[i] = si->r[i] - sj->r[j];

						// Sum of the dot product
						real RdotR = inner_product(rij.begin(), rij.end(), rij.begin(), init);
						real apre = 1./sqrt(RdotR * RdotR * RdotR);
						// Update accelerations
						for (int i = 0; i != 3; i++) {
							si->a[i] -= sj -> m*apre*rij[i];
						}
					}
				}
			}
		}

		void updatePositions(real dt) {
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++) {
				si->a0 = si->a;
				for (int i = 0; i != 3; i++) {
					si -> r[i] += dt*si->v[i] + 0.5*dt*dt*si->a0[i];
				}
			}
		}

		void updateVelocities(real dt) {
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++) {
				for (int i = 0; i != 3; i++) {
					si -> v[i] += 0.5*dt*(si->a0[i]+si->a[i]);
				}
				si->a0 = si->a;
			}
		}
			
		vector<real>energies() {
			real init = 0;
			vector <real> E(3), rij(3);
			E.assign(3,0);

			// Kinetic Energy
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++)
				E[1] += 0.5*si->m*inner_product(si->v.begin(), si->v.end(), si->v.begin(), init);
			// Potential Energy
			for (vector<Star>::iterator si = s.begin(); si != s.end(); si++) {
				for (vector<Star>::iterator sj = si+1; sj != s.end(); sj++) {
					for (int i = 0; i != 3; i++)
						rij[i] = si->r[i] - s[j]->r[i];
					E[2] -= si->m*sj->m/sqrt(inner_product(rij.begin(), rij.end(), rij.begin(), init));
				}
			}
			E[0] = E[1] + E[2];
			return E;
		}

		// Print Function
		friend ostream &operator << (ostream &so, Cluster &cl) {
			for (vector<Star>::iterator si = cl.s.begin(); si != cl.s.end(); si++) 
				so << *si;
			return so;
		}
};

int main() {
	Cluster cl;
	real m;
	int dummy;
	vector<real> r(3), v(3);

	do {
		cin >> dummy;
		cin >> m;
		for (int i = 0; i != 3; i++)
			cin >> r[i];
		for (int i = 0; i != 3; i++)
			cin >> v[i];
		cl.s.push_back(Star(m, r, v));
	}
	while (!cin.eof());
	
	cl.s.pop_back();

	vector<real> E(3), E0(3);
	E(0) = cl.energies();

	// https://en.cppreference.com/w/cpp/io/cerr
	// https://stackoverflow.com/questions/16772842/what-is-the-difference-between-cout-cerr-clog-of-iostream-header-in-c-when/16772906
	cerr << "Energies: " << E0[0] << " " << E0[1] << " " << E0[2] << endl;

	// Start time, end time and simulation step
	real t = 0.0;
	real tend = 1.0;
	real dt = 1e-3;
	int k = 0;

	// Initialize the accelerations
	cl.acceleration();

	while (t < tend) {
		cl.updatePositions(dt);
		cl.acceleration();
		cl.updateVelocities(dt);

		t += dt;
		k += 1;
		if (k%10 == 0) {
			E = cl.energies();
			cerr << "t= " << t << " E= "  << E[0] << " " << E[1] << " " << E[2] << " dE = " << (E[0]-E0[0])/E0[0] << endl;
		}
	}
	return 1;
}


