def reverse_between(self,start_index,end_index):
        if self.length == 0 or self.length == 1:
            return None
        else:
            current = self.head
            idx = 0 # Vai guardar o valor do índice do current, para poder comparar com os indices start e end. 
            first_reversed_node = None
            node_before_reversal = None
            prev_node = None
            next_node = current.next
            end = None
            end_of_reversal = None

            while current is not None:
                next_node = current.next  # Guarda sempre o próximo nó

                if idx == start_index - 1:
                    node_before_reversal = current  # Nó antes da secção a inverter

                if idx == start_index:
                    first_reversed_node = current  # Primeiro nó da secção a inverter

                if start_index <= idx <= end_index:
                    # Durante a inversão, atualiza os ponteiros
                    current.next = prev_node
                    prev_node = current

                if idx == end_index:
                    # Quando alcançamos o final da secção a inverter
                    if node_before_reversal is not None:
                        node_before_reversal.next = current  # Conecta o nó antes da secção ao último nó invertido

                    first_reversed_node.next = next_node  # Conecta o primeiro nó da secção ao nó após a inversão

                idx += 1
                current = next_node  # Atualiza o current para o próximo nó (já guardado)