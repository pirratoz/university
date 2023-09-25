pub use std::collections::HashMap;


pub type Edges = HashMap<usize, Vec<Point>>;


#[derive(Debug)]
#[derive(Clone)]
pub struct Point {
    pub v: usize,
    pub dist: i32
}


pub fn get_edges(_m: Vec<Vec<i32>>) -> Edges{
    let mut edges: Edges = HashMap::new();
    (0.._m.len()).for_each(|i| (0.._m.len()).for_each(|j| {
        if _m[i][j] != 0 {
            let mut e: Vec<Point> = if edges.contains_key(&i) {edges[&i].clone()} else {Vec::new()};
            e.push(Point{v: j, dist: _m[i][j]});
            edges.insert(i, e);
        }
    }));
    edges
}
