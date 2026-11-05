from .dfa import DFA
from .nfa import NFA

def nfa_to_dfa(A: NFA) -> DFA:
    """Algoritmo de conversão de um NFA para um DFA (determinização). A ideia se dá pela construção do 
    autômato potência de forma interativa a partir dos estados previamente alcançaveis dentro do workset.

    Args:
        A (NFA): Autômato finito não-determinístico a ser convertido em sua versão determinística.

    Returns:
        DFA: Autômato finito determinístico que reconhece a mesma linguagem de A.
    """
    Q = set()
    transition_table = {}
    F = set()
    S = A.alphabet
    q0 = A.initial_state

    states_name_dict = {frozenset({q0}):"q0"}
    i = 1
    # Função auxiliar necessária para trocar notação de conjunto {qi, ..., qj} por uma string "qk".
    def rename(state: frozenset) -> str:
        if state not in states_name_dict:
            nonlocal i
            states_name_dict[state] = f"q{i}"
            i += 1
        return states_name_dict[state] 

    workset = {frozenset({q0})}
    while workset:
        Q1 = workset.pop()
        Q.add(rename(Q1)) 
        if A.final_states_set & Q1:
            F.add(rename(Q1))
        for symbol in S:
            Q2 = set()
            for q in Q1:
                Q2 |= A.transition_table.get((q, symbol), set())
            Q2 = frozenset(Q2) 
            if not Q2:
                continue
            if rename(Q2) not in Q:
                workset.add(Q2)
            transition_table[(rename(Q1), symbol)] = rename(Q2)
    return DFA(Q, S, transition_table, "q0", F)