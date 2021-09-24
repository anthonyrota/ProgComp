/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var deepestLeavesSum = function (root) {
    if (!root) {
        return 0;
    }
    let deepestLevel = 0;
    let deepestLevelSum = 0;
    function visitNode(node, depth) {
        if (depth > deepestLevel) {
            deepestLevel = depth;
            deepestLevelSum = 0;
        }
        if (!node.left && !node.right) {
            if (depth === deepestLevel) {
                deepestLevelSum += node.val;
            }
            return;
        }
        if (node.left) {
            visitNode(node.left, depth + 1);
        }
        if (node.right) {
            visitNode(node.right, depth + 1);
        }
    }
    visitNode(root, 0);
    return deepestLevelSum;
};
