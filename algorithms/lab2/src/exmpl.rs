struct Graph {
    adjacency_matrix: Vec<Vec<i32>>,
    reachability_matrix: Vec<Sec<i32>>,
    shortest_path_weights: Vec<Vec<i32>>,
    predecessors: Vec<Vec<Option<usize>>>,
    excentricities: Vec<i32>,
}

impl Graph {
    fn new(adjacency_matrix: Vec<Vec<i32>>) -> Self {
        let n = adjacency_matrix.len();
        let reachability_matrix = adjacency_matrix.clone();
        let shortest_path_weights = adjacency_matrix.clone();
        let predecessors = vec![vec![None; n]; n];
        let excentricities = vec![0; n];
        Self {
            adjacency_matrix,
            reachability_matrix,
            shortest_path_weights,
            predecessors,
            excentricities,
        }
    }
    fn warshall(&mut self) {
        let reachability_matrix_clone = self.reachability_matrix.clone();
        self.reachability_matrix
            .iter_mut()
            .enumerate()
            .for_each(|(i, row)| {
                row.iter_mut().enumerate().for_each(|(j, cell)| {
                    *cell = (*cell > 0
                        || (reachability_matrix_clone[i][j] > 0
                            && reachability_matrix_clone[j][i] > 0))
                        as i32;
                });
            });
    }

    fn floyd_warshall(&mut self) {
        let n = self.adjacency_matrix.len();
        for k in 0..n {
            for i in 0..n {
                for j in 0..n {
                    if self.shortest_path_weights[i][k] != i32::MAX
                        && self.shortest_path_weights[k][j] != i32::MAX
                        && (self.shortest_path_weights[i][j]
                            > self.shortest_path_weights[i][k] + self.shortest_path_weights[k][j])
                    {
                        self.shortest_path_weights[i][j] =
                            self.shortest_path_weights[i][k] + self.shortest_path_weights[k][j];
                        self.predecessors[i][j] = Some(k);
                    }
                }
            }
        }
    }

    fn calculate_excentricities(&mut self) {
        let n = self.adjacency_matrix.len();
        for i in 0..n {
            for j in 0..n {
                if i != j && self.shortest_path_weights[i][j] != i32::MAX {
                    self.excentricities[i] += 1;
                }
            }
        }
    }

    fn print_option_matrix(message: &str, matrix: &[Vec<Option<usize>>]) {
        println!("{}", message);
        matrix
            .iter()
            .for_each(|sub_matrix| println!("{:?}", sub_matrix))
    }

    fn print_matrix(message: &str, matrix: &[Vec<i32>]) {
        println!("{}", message);
        matrix
            .iter()
            .for_each(|sub_matrix| println!("{:?}", sub_matrix))
    }

    fn print_matrices(&self) {
        Self::print_matrix("Main matrix:", &self.adjacency_matrix);
        Self::print_matrix("Warshell matrix:", &self.reachability_matrix);
        Self::print_matrix("Weights matrix:", &self.shortest_path_weights);
        Self::print_option_matrix("Previous matrix:", &self.predecessors);
    }

    fn print_graph_properties(&self) {
        let r = *self.excentricities.iter().min().unwrap();
        let d = *self.excentricities.iter().max().unwrap();
        let mids: Vec<_> = (0..self.excentricities.len())
            .filter(|&i| self.excentricities[i] == r)
            .collect();
        println!(
            "R={}\nD={}\nmid's={:?}\ne={:?}",
            r, d, mids, self.excentricities
        );
    }

    fn get_shortest_path(&self, start: usize, end: usize) -> Option<Vec<usize>> {
        let mut path = vec![];
        let mut current_vertex = Some(start);

        while let Some(vertex) = current_vertex {
            path.push(vertex);
            current_vertex = self.predecessors[vertex][end];

            if path.len() > 1 && path[0] == path[1] {
                return None;
            }

            if path.len() >= 2 && path[path.len() - 1] == path[path.len() - 2] {
                return None;
            }

            if vertex == end {
                break;
            }
        }

        Some(path)
    }
}

fn main() {
    let m = vec![
        vec![0, 0, 5, 0, 0],
        vec![7, 0, 0, 0, 10],
        vec![0, 7, 0, 0, 0],
        vec![0, 0, 3, 0, 4],
        vec![0, 0, 1, 0, 0],
    ];

    let mut graph = Graph::new(m);

    graph.warshall();
    graph.floyd_warshall();
    graph.calculate_excentricities();
    graph.print_matrices();
    println!();
    graph.print_graph_properties();
    println!();

    match graph.get_shortest_path(3, 0) {
        Some(path) => println!(
            "Маршрут: {:?}\nДлина маршрута: {}",
            path, graph.shortest_path_weights[3][0]
        ),
        None => println!("Маршрут не существует"),
    }
}
