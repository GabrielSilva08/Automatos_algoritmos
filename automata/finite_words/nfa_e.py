class NFA_e:
    """Autômato Finito Não-determinístico com transições vazias (Nondeterministic Finite Automaton with e-transitions) dado pela definição clássica (Q, Σ, δ, q0, F).
    O simbolo representando a transição vazia será "e".
    """
    def __init__(self,
                 states_set: set[str],
                 alphabet: set[str|int],
                 transition_table: dict[tuple[str, str|int], set[str]],
                 initial_state: str,
                 final_states_set: set[str]):
        """Método construtor da classe.

        Args:
            states_set (set[str]): Conjunto não vazio de estados.
            alphabet (set[str | int]): Alfabeto na qual o autômato irá operar. Ex: Σ = {a, b}.
            transition_table (dict[tuple[str, str | int], set[str]]): Tabela de transição. Estrutura responsável por modelar a função de transição δ : Q × (Σ ∪ {e}) → P(Q).
            initial_state (str): Estado inicial. Ex: "q0".
            final_states (set[str]): Conjunto de estados finais, onde final_states ⊆ states_set.
        """
        self.states_set = states_set
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.final_states_set = final_states_set
        self._validate()

    def __repr__(self) -> str:
        """Representação do autômato para fins de depuração.

        Returns:
            str: Tupla contendo os elementos internos do NFA_e.
        """
        return f"NFA_e(Q = {self.states_set},\nΣ = {self.alphabet},\nδ = {self.transition_table},\nq0 = {self.initial_state},\nF = {self.final_states_set})"

    def eval(self, word: str) -> bool:
        pass

    def union(self):
        pass

    def intersection(self):
        pass

    def difference(self):
        pass

    def complement(self):
        pass

    def language(self):
        pass

    def is_empty(self):
        pass

    def is_equivalent_to(self):
        pass

    def _validate(self):
        """Realiza uma série de verificações para garantir que os argumentos passados no construtor formem um NFA_e consistente.
        """
        if not self.states_set:
            raise ValueError("The set of states cannot be empty.")
        
        if self.initial_state not in self.states_set:
            raise ValueError("The initial state must belong to the set of states.")
        
        if not (self.final_states_set <= self.states_set):
            raise ValueError("Final states must belong to the set of states.")

        for (state, symbol), states_set in self.transition_table.items():
            if state not in self.states_set:
                raise ValueError(f"Unknown source state: {state}")

            if symbol not in (self.alphabet | {"e"}):
                raise ValueError(f"Unknown symbol: {symbol}")

            if not (states_set <= self.states_set):
                raise ValueError(f"Unknown destination states_set: {states_set}")

    def _check_word_in_alphabet(self, word: str) -> bool:
        """Verifica se os simbolos que compõem a palavra estão todos presentes no alfabeto do autômato.

        Args:
            word (str): Palavra a ser verificada

        Returns:
            bool: True se word ∈ Σ*, False caso contrário.
        """
        return all(symbol in self.alphabet for symbol in word)
