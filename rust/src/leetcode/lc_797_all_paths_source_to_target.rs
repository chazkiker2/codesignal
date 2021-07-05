use std::collections::{HashMap, HashSet, VecDeque};
use std::convert::TryInto;
use std::iter::FromIterator;

/// https://leetcode.com/problems/all-paths-from-source-to-target/
pub struct LeetCode797;

impl LeetCode797 {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut all_paths = vec![];

        if graph.is_empty() {
            return all_paths;
        }

        let mut map: HashMap<i32, HashSet<i32>> = HashMap::with_capacity(graph.len());

        for i in 0..graph.len() {
            map.insert(i as i32, HashSet::from_iter(graph[i].iter().cloned()));
        }

        let mut deque: VecDeque<(i32, Vec<i32>)> = VecDeque::new();
        deque.push_back((0, vec![]));

        while let Some((current_node, current_path_ref)) = deque.pop_back() {
            let mut current_path: Vec<i32> = current_path_ref.iter().cloned().collect();
            current_path.push(current_node);

            if map.get(&current_node).unwrap().len() < 1 {
                all_paths.push(current_path.iter().cloned().collect());
            }

            if let Some(edges) = map.get(&current_node) {
                for edge in edges {
                    deque.push_back((*edge, current_path.iter().cloned().collect()))
                }
            }
        }

        let target_node: i32 = graph.len().try_into().unwrap();
        let target_node: i32 = target_node - 1;
        let valid_paths = all_paths
            .into_iter()
            .filter(|path| path[0] == 0 && path[path.len() - 1] == target_node)
            .collect();
        valid_paths
    }
}

#[cfg(test)]
mod tests {
    use super::LeetCode797;

    fn vec_compare(va: Vec<Vec<i32>>, vb: Vec<Vec<i32>>) -> bool {
        let mut va = va.clone();
        let mut vb = vb.clone();

        va.sort();
        vb.sort();

        let eq = (va.len() == vb.len())
            && va.iter().zip(vb.clone()).all(|(a, b)| {
                let mut a = a.clone();
                let mut b = b.clone();

                a.sort();
                b.sort();

                (a.len() == b.len()) && a.iter().zip(b).all(|(an, bn)| *an == bn)
            });
        if !eq {
            println!(
                "EXPECTED: len={}{:#?}\nACTUAL: len={}{:#?}",
                va.len(),
                va,
                vb.len(),
                vb
            );
        }
        eq
    }

    #[test]
    fn leet_code_797_001() {
        let input = vec![vec![1, 2], vec![3], vec![3], vec![]];
        let actual = LeetCode797::all_paths_source_target(input);
        let expected = vec![vec![0, 1, 3], vec![0, 2, 3]];
        assert!(vec_compare(expected, actual));
    }

    #[test]
    fn leet_code_797_002() {
        let input = vec![vec![4, 3, 1], vec![3, 2, 4], vec![3], vec![4], vec![]];
        let expected = vec![
            vec![0, 1, 3],
            vec![0, 2, 3],
            vec![0, 1, 2, 3, 4],
            vec![0, 1, 3, 4],
            vec![0, 1, 4],
            vec![0, 3, 4],
            vec![0, 4],
        ];
        let actual = LeetCode797::all_paths_source_target(input);
        assert!(vec_compare(expected, actual));
    }

    #[test]
    fn leet_code_797_003() {
        let input = vec![vec![1], vec![]];
        let expected = vec![
            vec![0, 1, 3],
            vec![0, 2, 3],
            vec![0, 1, 2, 3, 4],
            vec![0, 1, 3, 4],
            vec![0, 1, 4],
            vec![0, 3, 4],
            vec![0, 4],
            vec![0, 1],
        ];
        let actual = LeetCode797::all_paths_source_target(input);
        assert!(vec_compare(expected, actual));
    }

    #[test]
    fn leet_code_797_004() {
        let input = vec![vec![4, 3, 1], vec![3, 2, 4], vec![], vec![4], vec![]];
        let expected = vec![vec![0, 4], vec![0, 3, 4], vec![0, 1, 3, 4], vec![0, 1, 4]];
        let actual = LeetCode797::all_paths_source_target(input);
        assert!(vec_compare(expected, actual));
    }
}
