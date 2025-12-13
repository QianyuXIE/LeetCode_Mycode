def recover_tree(preorder, inorder):
    if len(preorder)==0:
        return ""

    root = preorder[0]
    idx_root = inorder.index(root)

    in_left = inorder[:idx_root]
    in_right = inorder[idx_root+1:]

    left_size = len(in_left)
    pre_left = preorder[1:1+left_size]
    pre_right = preorder[1+left_size:]

    post_left = recover_tree(pre_left, in_left)
    post_right = recover_tree(pre_right, in_right)

    return post_left + post_right + root


while True:
    try:
        T_pre, T_in = input().split()
        print(recover_tree(T_pre, T_in))
    except EOFError:
        break