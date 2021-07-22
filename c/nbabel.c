#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef double real;
typedef real real3[3];

// Global Variables
int n;               // number of particles
real *m;             // masses
real3 *r;            // position
real3 *v;            // velocity
real3 *a;            // acceleration
real3 *a0;           // previous acceleration

void acceleration() {
	// Reset acceleration
	for(int i=0; i < n; i++) {
		a[i][0] = a[i][1] = a[i][2] = 0;
	}

	// For each star
	for (int i=0; i < n; i++) {
		real rij[3];
		
		// for each remaining star
		for (int j = 0; j < n; j++) {
			if(i != j) {
				rij[0] = r[i][0] - r[j][0];
				rij[1] = r[i][1] - r[j][1];
				rij[2] = r[i][2] - r[j][2];

				real RdotR = (rij[0] * rij[0] + rij[1] * rij[1] + rij[2] * rij[2]);
				real apre = 1.0/sqrt(RdotR * RdotR * RdotR);

				// Update acceleration
				a[i][0] -= m[j]*apre*rij[0];
				a[i][1] -= m[j]*apre*rij[1];
				a[i][2] -= m[j]*apre*rij[2];

			}
		}
	}
}

// Update position
void updatePositions(real dt) {
	for (int i=0; i < n; i++) {
		a0[i][0] = a[i][0];
		a0[i][1] = a[i][1];
		a0[i][2] = a[i][2];

		r[i][0] += dt*v[i][0] + 0.5 * dt * dt * a0[i][0];
		r[i][1] += dt*v[i][1] + 0.5 * dt * dt * a0[i][1];
		r[i][2] += dt*v[i][2] + 0.5 * dt * dt * a0[i][2];

	}
}

// Update velocities
void updateVelocities(real dt) { 
	for (int i=0; i < n; i++) {
		v[i][0] += 0.5 * dt * (a0[i][0] + a[i][0]);
		v[i][1] += 0.5 * dt * (a0[i][1] + a[i][1]);
		v[i][2] += 0.5 * dt * (a0[i][2] + a[i][2]);

		a0[i][0] = a[i][0];
		a0[i][1] = a[i][1];
		a0[i][2] = a[i][2];
	}
}

// Energy
void energies(real *kinetic_energy, real *potential_energy) {
	real rij[3];
	real ke = 0;
	real pe = 0;

	// Kinetic Energy
	for (int i=0; i < n; i++) {
		ke += 0.5 * m[i] * (v[i][0] * v[i][0] + v[i][1] * v[i][1] + v[i][2] * v[i][2]);
	}

	// Potential Energy
	for (int i=0; i < n; i++) {
		for (int j=i+1; j < n; j++) {
			rij[0] = r[i][0] - r[j][0];
			rij[1] = r[i][1] - r[j][1];
			rij[2] = r[i][2] - r[j][2];
			
			pe -= m[i] * m[j] / sqrt((rij[0]*rij[0] + rij[1]*rij[1] + rij[2]*rij[2]));
		}
	}
	*kinetic_energy = ke;
	*potential_energy = pe;
}

int main() {
	int memory_size = 16384;
	m = (real*)malloc(sizeof(real)*memory_size);
	r = (real3*)malloc(sizeof(real3)*memory_size);
	v = (real3*)malloc(sizeof(real3)*memory_size);
	a = (real3*)malloc(sizeof(real3)*memory_size);
	a0 = (real3*)malloc(sizeof(real3)*memory_size);
	
	real mass;
	int dummy;

	real rx, ry, rz, vx, vy, vz;

	int count=0;
	while (scanf("%d %lf %lf %lf %lf %lf %lf %lf\n", &dummy, &mass, &rx, &ry, &rz, &vx, &vy, &vz) != EOF) {
	       m[count] = mass;
       	       r[count][0] = rx;
	       r[count][1] = ry;
	       r[count][2] = rz;
	       v[count][0] = vx;
	       v[count][1] = vy;
	       v[count][2] = vz;

	       count++;
	       if(count == memory_size) {
		       memory_size += 1024;
		       m = (real*)realloc(m, sizeof(real)*memory_size);
		       r = (real3*)realloc(r, sizeof(real3)*memory_size);
		       v = (real3*)realloc(r, sizeof(real3)*memory_size);
		       a = (real3*)realloc(r, sizeof(real3)*memory_size);
		       a0 = (real3*)realloc(r, sizeof(real3)*memory_size);
		}
	}

	n = count;
	real k_energy, p_energy, initial_total_energy;
	energies(&k_energy, &p_energy);
	printf("Energies: %lf %lf %lf \n", k_energy+p_energy, k_energy, p_energy);
	float total_energy = 0.0;
	total_energy = k_energy + p_energy;

	real t = 0.0;
	real tend = 1.0;
	real dt = 1e-3;
	int k = 0;

	// Initialize acceleration
	acceleration();

	while(t<tend) {
		updatePositions(dt);
		acceleration();
		updateVelocities(dt);

		t += dt;
		k += 1;
		if (k%10 == 0) {
			energies(&k_energy, &p_energy);
			real total_energy = k_energy + p_energy;
			real dE = (total_energy - initial_total_energy)/initial_total_energy;
			printf("t= %lg E=: %lg %lg %lg dE = %lg\n", t, total_energy, k_energy, p_energy, dE);
		}
	}
	return 1;
}	


