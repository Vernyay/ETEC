// ==========================================
// 1. CLASSE MÃE / SUPERCLASSE (ABSTRAÇÃO)
// ==========================================
class ContaBancaria {
  // Atributos privados (Encapsulamento)
  String _titular;
  double _saldo;

  // Construtor
  ContaBancaria(this._titular, this._saldo);

  // Getters para leitura segura dos dados
  String get titular => _titular;
  double get saldo => _saldo;

  // Métodos de negócio
  void depositar(double valor) {
    if (valor > 0) {
      _saldo += valor;
      print("Depósito de R\$ ${valor.toStringAsFixed(2)} realizado com sucesso!");
    } else {
      print("Valor de depósito inválido.");
    }
  }

  void sacar(double valor) {
    if (valor > 0 && valor <= _saldo) {
      _saldo -= valor;
      print("Saque de R\$ ${valor.toStringAsFixed(2)} realizado com sucesso!");
    } else {
      print("Saldo insuficiente ou valor inválido para saque.");
    }
  }

  void exibirExtrato() {
    print("--- EXTRATO ---");
    print("Titular: $_titular");
    print("Saldo atual: R\$ ${_saldo.toStringAsFixed(2)}");
  }
}

// ==========================================
// 2. CLASSE FILHA (HERANÇA E POLIMORFISMO)
// ==========================================
class ContaPoupanca extends ContaBancaria {
  int _diaAniversario;

  ContaPoupanca(String titular, double saldo, this._diaAniversario) 
      : super(titular, saldo);

  int get diaAniversario => _diaAniversario;

  // Sobrescrita de método (Polimorfismo)
  @override
  void exibirExtrato() {
    print("=== EXTRATO CONTA POUPANÇA ===");
    print("Titular: $titular");
    print("Dia do Rendimento: $_diaAniversario");
    print("Saldo atual: R\$ ${saldo.toStringAsFixed(2)}");
    print("================================");
  }

  // Método específico da Poupança
  void renderJuros(double taxa) {
    double juros = saldo * (taxa / 100);
    depositar(juros);
    print("Rendimento de R\$ ${juros.toStringAsFixed(2)} aplicado!");
  }
}

// ==========================================
// 3. FUNÇÃO PRINCIPAL (EXECUÇÃO)
// ==========================================
void main() {
  print("=== SISTEMA BANCÁRIO ===");

  // Criando um objeto do tipo ContaBancaria
  print("\n[Criando Conta Comum]");
  var contaComum = ContaBancaria("Carlos Silva", 500.0);
  contaComum.depositar(200.0);
  contaComum.sacar(100.0);
  contaComum.exibirExtrato();

  // Criando um objeto do tipo ContaPoupanca (Herança)
  print("\n[Criando Conta Poupança]");
  var contaPoup = ContaPoupanca("Ana Souza", 1200.0, 15);
  contaPoup.renderJuros(1.0); // Aplica 1% de juros
  contaPoup.exibirExtrato(); // Executa o método polimórfico sobrescrito
}