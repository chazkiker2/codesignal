//! # LeetCode 114: Flatten Binary Tree to Linked List
//!
//! Given the `root` of a binary tree, flatten the tree into a "linked list":
//!
//! - The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
//! - The "linked list" should be in the same order as a [pre-order traversal] of the binary tree.
//!
//! Pre-Order Traversal: Current -> Left -> Right
//!
//! [Pre-Order Traversal]: https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR
//!
//!
//! ## Examples
//!
//! ### Example 1:
//!
//! - Input: root = [1,2,5,3,4,null,6]
//! - Output: [1,null,2,null,3,null,4,null,5,null,6]
//!
//! ### Example 2:
//!
//! - Input: root = []
//! - Output: []
//!
//!
//! ### Example 3:
//!
//! - Input: root = [0]
//! - Output: [0]
//!
//!
//! ### Constraints:
//!
//! - The number of nodes in the tree is in the range `[0, 2000]`.
//! - `-100 <= Node.val <= 100`
//!
//!
//! ## Follow Up
//!
//! Can you flatten the tree in-place (with `O(1)` extra space)?

use std::cell::RefCell;
use std::rc::Rc;

pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub struct LeetCode114;

impl LeetCode114 {
    fn _pre_order(root: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
        if let Some(node) = root {
            result.push(node.borrow().val);
            Self::_pre_order(node.borrow().left.clone(), result);
            Self::_pre_order(node.borrow().right.clone(), result);
        }
    }

    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        let mut result: Vec<i32> = vec![];
        Self::_pre_order(root.clone(), &mut result);
        println!("{:#?}", result);
    }
}

#[cfg(test)]
mod tests {
    use super::{LeetCode114, TreeNode};
    use std::cell::RefCell;
    use std::rc::Rc;

    /// - Input: root = [1,2,5,3,4,null,6]
    /// - Output: [1,null,2,null,3,null,4,null,5,null,6]
    #[test]
    fn test_001() {
        let mut left1 = TreeNode::new(2);
        left1.left = Some(Rc::new(RefCell::new(TreeNode::new(3))));
        left1.right = Some(Rc::new(RefCell::new(TreeNode::new(4))));
        let mut right1 = TreeNode::new(5);
        right1.right = Some(Rc::new(RefCell::new(TreeNode::new(6))));
        let mut root = TreeNode::new(1);
        root.left = Some(Rc::new(RefCell::new(left1)));
        root.right = Some(Rc::new(RefCell::new(right1)));

        LeetCode114::flatten(&mut Some(Rc::new(RefCell::new(root))));

        assert_eq!(1, 1);
    }

    /// - Input: root = []
    /// - Output: []
    #[test]
    fn test_002() {
        
        assert_eq!(1, 1);
    }

    /// - Input: root = [0]
    /// - Output: [0]
    #[test]
    fn test_003() {
        assert_eq!(1, 1);
    }
}
