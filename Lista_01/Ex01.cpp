#include <iostream>

using namespace std;

int main() {
    cout << "Digite seu nome: ";
    string nome;
    cin >> nome;
    cout << "Olá, " << nome << endl;
    return 0;
}

// Para compilar: g++ Ex01.cpp -o Ex01