#[allow(dead_code)]
use std::collections::HashMap;

/// https://leetcode.com/problems/all-paths-from-source-to-target/
struct LeetCode797;
impl LeetCode797 {
    #[allow(dead_code)]
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let map: HashMap<i32, Vec<i32>> = HashMap::new();
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn leet_code_797_001() {
        assert_eq!(2 + 2, 4);
    }
}
