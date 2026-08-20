# MNIST Basics — Questions & Answers

---

## 1. How is a grayscale image represented on a computer? How about a color image?

Images are represented by arrays with pixel values representing the content of the image. For grayscale images, a 2-dimensional array is used with the pixels representing the grayscale values, with a range of 256 integers. A value of 0 represents black, and a value of 255 represents white, with different shades of gray in between. For color images, three color channels (red, green, blue) are typically used, with a separate 256-range 2D array used for each channel. A pixel value of 0 represents black, with 255 representing solid red, green, or blue. The three 2D arrays form a final 3D array (rank 3 tensor) representing the color image.

---

## 2. How are the files and folders in the `MNIST_SAMPLE` dataset structured? Why?

```
MNIST_SAMPLE/
├── train/          ← images used for training
│   ├── 3/          ← all images of the digit "3" (folder name = label)
│   │   ├── 1.png
│   │   └── ...
│   └── 7/          ← all images of the digit "7"
│       ├── 1.png
│       └── ...
└── valid/          ← images held out for evaluation
    ├── 3/
    └── 7/
```

**Why?** This is called an **"ImageFolder" layout** — the folder *name* IS the label. It means a data-loading utility (like `ImageDataLoaders.from_folder`) can scan the folders and automatically associate each image with its class, with zero manual annotation. It's also split into `train`/`valid` so we can train on one set and honestly evaluate performance on images the model has never seen.

---

## 3. Explain how the "pixel similarity" approach to classifying digits works.

1. Take all training images of a digit (say, "3") and compute the **average pixel value at each position** across all of them → this produces a single **"ideal 3"** image (the mean image, also called a prototype).
2. Do the same for "7" → an **"ideal 7"** image.
3. To classify a *new* image, measure how **different** it is from each ideal image using a distance metric such as the **L1 norm** (`mean(abs(a - b))`) or **RMSE**. 
4. Whichever ideal image has the **smallest distance** to the new image "wins" — that's the predicted digit.

It's a great *baseline*: no learning, no parameters, yet it gets ~95%+ accuracy on MNIST 3-vs-7.

---

## 4. What is a list comprehension? Create one now that selects odd numbers from a list and doubles them.

A list comprehension is a compact Python syntax for building a list by transforming/filtering items from an existing iterable.

```python
numbers = [1, 2, 3, 4, 5, 6]
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print(doubled_odds)  # [2, 6, 10]
```

Structure: `[expression for item in iterable if condition]`.

---

## 5. What is a "rank-3 tensor"?

A tensor's **rank** is the number of axes (dimensions) it has. A rank-3 tensor is simply a 3-dimensional array — a "cube" of numbers indexed by `(i, j, k)`.

Examples:
- A color image of shape `(height, width, 3)` — 2 spatial axes + 1 color-channel axis.
- A batch of grayscale images of shape `(num_images, height, width)`.

```python
import torch
t = torch.zeros(4, 28, 28)
print(t.ndim)   # 3  → rank-3 tensor
```

---

## 6. What is the difference between tensor rank and shape? How do you get the rank from the shape?

- **Rank** = number of axes/dimensions.
- **Shape** = the size (length) along each axis.

| Tensor | Rank | Shape |
|--------|------|-------|
| `[1,2,3]` | 1 | `(3,)` |
| `[[1,2],[3,4]]` | 2 | `(2,2)` |
| batch of 10 color images | 3 | `(10,28,28,3)` |

**Rank is just `len(shape)`:**

```python
t = torch.randn(10, 3, 28, 28)
shape = t.shape          # torch.Size([10, 3, 28, 28])
rank = len(shape)        # 4
```

---

## 7. What are RMSE and L1 norm?

Given a vector of differences (prediction − actual):

- **L1 norm** = mean of the absolute values:
  `L1 = mean(|aᵢ − bᵢ|)`
- **RMSE** (Root Mean Squared Error) = square root of the mean of squared differences:
  `RMSE = sqrt( mean((aᵢ − bᵢ)²) )`

RMSE punishes large errors more heavily (because of the squaring). L1 is more robust to outliers.

---

## 8. How can you apply a calculation on thousands of numbers at once, many thousands of times faster than a Python loop?

Use **vectorized operations** with NumPy arrays or PyTorch tensors. The heavy arithmetic runs in compiled C/Fortran code (not an interpreted Python loop), and it can use SIMD instructions and even GPUs. Example:

```python
import torch
a = torch.randn(1_000_000)
b = torch.randn(1_000_000)

# Python loop: slow
# for i in range(len(a)): c[i] = a[i] * b[i]

# Vectorized: fast
c = a * b
```

---

## 9. Create a 3×3 tensor or array containing the numbers from 1 to 9. Double it. Select the bottom-right four numbers.

```python
import torch

a = torch.tensor([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
b = a * 2
c, d = a[1][1:], a[2][1:]
e = torch.stack((c,d))

# OR

t = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

t = t * 2                    # double it
# tensor([[ 2,  4,  6],
#         [ 8, 10, 12],
#         [14, 16, 18]])

bottom_right = t[1:, 1:]     # rows 1+, cols 1+
# tensor([[10, 12],
#         [16, 18]])
```

---

## 10. What is broadcasting?

Broadcasting lets you do element-wise operations on tensors of *different* shapes by automatically "stretching" the smaller tensor to match the larger one — **without copying data**.

Rules: align shapes from the right; each dimension must match, be 1, or be missing.

```python
a = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])      # shape (2, 3)
b = torch.tensor([10, 20, 30])     # shape (3,) → broadcast to (2, 3)

print(a + b)
# tensor([[11, 22, 33],
#         [14, 25, 36]])
```

Here `b` is stretched along the missing row axis. This is how we add a bias vector to every image in a batch.

---

## 11. Are metrics generally calculated using the training set, or the validation set? Why?

The **validation set**. Metrics exist to tell us how well the model will perform on *new, unseen* data. The model has already "memorized" the training set, so training accuracy is misleadingly high. Only the validation set gives an honest estimate of generalization.

---

## 12. What is SGD?

**SGD** = **Stochastic Gradient Descent**. It's the optimization algorithm that trains the model:

1. Look at a small random batch of data.
2. Compute the loss (how wrong the predictions are).
3. Compute the **gradient** — the direction of steepest *increase* of the loss with respect to each weight.
4. Move each weight a small step in the *opposite* direction (downhill) to decrease the loss.

"Stochastic" because each step uses a random mini-batch, so the estimate of the true gradient is noisy — which is actually a feature (helps escape local minima).

---

## 13. Why does SGD use mini-batches?

- The full dataset is too big to compute the gradient over all samples at once (memory + time).
- A mini-batch gives a **good, noisy estimate** of the true gradient — fast to compute.
- The noise helps the optimizer **escape local minima** and can lead to better generalization.
- It naturally enables **GPU parallelism** (many samples processed at once).

---

## 14. What are the seven steps in SGD for machine learning?

1. **Initialize** the weights randomly.
2. For each image: **predict** using the current weights (forward pass).
3. **Calculate the loss** — how wrong the prediction was.
4. **Calculate the gradient** of the loss with respect to each weight.
5. **Update the weights**: `w ← w − lr · gradient` (step downhill).
6. **Repeat** steps 2–5 until the end of the epoch (all batches seen).
7. **Stop** when the model is good enough (e.g., validation loss stops improving).

---

## 15. How do we initialize the weights in a model?

**Randomly**, with small values. PyTorch's `nn.Linear` uses **Kaiming (He) initialization**: weights are drawn from a uniform/normal distribution scaled by the number of inputs (fan-in) so that activations don't explode or vanish.

Why random? If all weights started equal, every neuron would update identically (symmetry), and the network couldn't learn diverse features. Small random values break the symmetry while keeping the training stable.

---

## 16. What is "loss"?

The **loss** is a single number that measures how *wrong* the model's predictions are on a batch of data — i.e., the distance between predictions and true labels. It must be **differentiable** so we can compute gradients. Lower loss = better model. Example: cross-entropy loss for classification.

---

## 17. Why can't we always use a high learning rate?

If the learning rate is **too high**, each weight update overshoots the minimum — the loss **bounces around or diverges** (explodes to infinity). If it's **too low**, training crawls and takes forever.

The right learning rate is a careful balance. `lr = 0.1` in fast.ai is a reasonable default; values like `1e-1` vs `1e-3` can be the difference between learning and diverging.

---

## 18. What is a "gradient"?

The **gradient** is the vector of partial derivatives of the loss with respect to each weight:
`∇L = (∂L/∂w₁, ∂L/∂w₂, ..., ∂L/∂wₙ)`.

It points in the direction of **steepest increase** of the loss. To *minimize* the loss, we move the weights in the **opposite** direction of the gradient.

---

## 19. Do you need to know how to calculate gradients yourself?

**No.** PyTorch's automatic differentiation (**autograd**) computes all gradients for you. You only need to call:

```python
loss.backward()
```

and each weight's gradient is stored in `w.grad`. (You *do* need to understand the *concept* of gradients to use them well, but not the calculus.)

---

## 20. Why can't we use accuracy as a loss function?

Accuracy is **not differentiable**:

- It's computed with an `argmax` (discrete prediction → compare to label), so it's a piecewise-constant function.
- Tiny changes in weights almost never change accuracy → the gradient is **0 (or undefined) almost everywhere**.
- With no gradient, gradient descent can't learn.

Loss functions like cross-entropy are **smooth and continuous**, so every small weight change moves the loss a little and gives a useful gradient.

---

## 21. Draw the sigmoid function. What is special about its shape?

```
sigmoid(x) = 1 / (1 + e⁻ˣ)

        1 ──────────────────────────•
         |                        ..|
         |                      ..  |
         |                    ..    |
         |                ...       |
         |           .....          |
         |     ......               |
         |  ...                     |
        0 ────•─────────────────────
             -4    -2    0    2    4
```

**Shape:** It's an **S-curve** (sigmoidal). It's:
- Smooth and differentiable everywhere
- Bounded between **0 and 1** (great for probabilities)
- **Flat** near 0 and 1 (gradient → 0), **steep** in the middle around x=0

---

## 22. What is the difference between a loss function and a metric?

- **Loss function**: differentiable, used *by the optimizer* for gradient descent. It's what gets minimized.
- **Metric**: human-readable measure of performance (accuracy, RMSE), used to *communicate* how well the model works.

They can be the same thing, but often aren't (e.g., loss = cross-entropy, metric = accuracy).

---

## 23. What is the function to calculate new weights using a learning rate?

```
new_weight = weight − lr · gradient
```

In code:

```python
w.data -= lr * w.grad
# or, equivalently:
w = w - lr * w.grad
```

The learning rate `lr` controls the step size.

---

## 24. What does the `DataLoader` class do?

`DataLoader` wraps a dataset and provides:
- **Mini-batches** (grouped samples of a fixed batch size)
- **Shuffling** each epoch (so batches are random)
- **Multiprocessing** for fast loading
- Parallel iteration: `for xb, yb in dl:`

In fast.ai, `dls.train` and `dls.valid` are DataLoaders that yield batches of inputs `xb` and labels `yb`.

---

## 25. Write pseudocode showing the basic steps taken in each epoch for SGD.

```python
for epoch in range(n_epochs):
    for xb, yb in train_dl:          # 1. grab a random mini-batch
        preds = model(xb)            # 2. forward pass: predictions
        loss = loss_func(preds, yb)  # 3. compute the loss
        loss.backward()              # 4. compute gradients
        opt.step()                   # 5. update weights: w -= lr * grad
        opt.zero_grad()              # 6. reset gradients to 0
```

---

## 26. Create a function that, if passed two arguments `[1,2,3,4]` and `'abcd'`, returns `[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]`. What is special about that output data structure?

```python
def pair(a, b):
    return list(zip(a, b))

print(pair([1, 2, 3, 4], 'abcd'))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

**Special:** the output is a **list of tuples**. Each tuple *pairs* the i-th element of the first argument with the i-th element of the second (`zip` does this). Tuples are **immutable** grouped values — ideal for representing a fixed relationship between two items.

---

## 27. What does `view` do in PyTorch?

`view` **reshapes** a tensor (same data, new shape) *without copying* it, as long as the total number of elements is unchanged and the tensor is contiguous.

```python
x = torch.randn(64, 28, 28)
x2 = x.view(64, -1)   # flatten last two dims → shape (64, 784)
```

`-1` means "infer this dimension from the others." This is how 28×28 images become 784-pixel vectors for `nn.Linear(784, 10)`.

---

## 28. What are the "bias" parameters in a neural network? Why do we need them?

The bias `b` is the additive constant in each neuron:
`z = Σ wᵢxᵢ + b`.

**Why needed:** without a bias, the layer's output is forced through the origin (when input is all zeros, output must be 0). The bias shifts the function so the layer can represent *any* line/plane, giving it much more flexibility. It's also how a neuron can "fire" even when all inputs are zero.

---

## 29. What does the `@` operator do in Python?

It's **matrix multiplication**:

```python
z = x @ w      # equivalent to torch.matmul(x, w)

x: (batch, in)  @  w: (in, out)  →  z: (batch, out)
```

For a linear layer: `z = x @ w.T + b` (PyTorch stores weights transposed as `(out, in)`).

---

## 30. What does the `backward` method do?

`loss.backward()` runs **backpropagation**: it computes the derivative of the loss with respect to **every** tensor with `requires_grad=True` and stores the result in each tensor's `.grad` attribute.

```python
loss.backward()
w.grad   # now holds d(loss)/d(w)
```

It uses the chain rule to propagate gradients backward through the computation graph.

---

## 31. Why do we have to zero the gradients?

Gradients **accumulate** by default — each `backward()` call *adds* to the existing `.grad` rather than replacing it. If you don't reset them, every step would use the **sum of gradients from all previous steps**, which corrupts the update.

```python
opt.zero_grad()   # sets all .grad to zero before the next backward()
loss.backward()   # now .grad holds only this batch's gradient
opt.step()
```

---

## 32. What information do we have to pass to `Learner`?

In fast.ai, `Learner` needs:

- **`dls`** — the DataLoaders (train + valid)
- **`model`** — an `nn.Module` (the architecture)
- **`loss_func`** — the loss function (e.g., `CrossEntropyLossFlat`)
- **`metrics`** — e.g., `accuracy`
- **`opt_func`** — the optimizer (defaults to SGD/Adam)

```python
learn = Learner(dls, model, loss_func=CrossEntropyLossFlat(), metrics=accuracy)
```

---

## 33. Show Python or pseudocode for the basic steps of a training loop.

```python
def train_epoch(model, train_dl, loss_func, opt):
    model.train()
    for xb, yb in train_dl:
        preds = model(xb)              # forward
        loss = loss_func(preds, yb)    # loss
        loss.backward()                # gradients
        opt.step()                     # update weights
        opt.zero_grad()                # reset gradients

for epoch in range(n_epochs):
    train_epoch(model, train_dl, loss_func, opt)
    valid_loss = validate(model, valid_dl, loss_func)   # check on validation
```

---

## 34. What is "ReLU"? Draw a plot of it for values from `-2` to `+2`.

```
ReLU(x) = max(0, x)

       2 ───────────────────────────────•
        |                              /
        |                            /
        |                          /
       1 ─────────────────────────•
        |                        /
        |                      /
       0 ────••••••••••••••••••
            -2   -1    0    1    2
```

For `x ≤ 0`, ReLU outputs `0` (flat). For `x > 0`, it outputs `x` (a straight line). It's the most common **activation function** in modern neural networks — cheap, and its gradient (0 or 1) avoids the "vanishing gradient" problem of sigmoid.

---

## 35. What is an "activation function"?

An activation function is a **nonlinear** function applied to the output of a linear layer:

```
output = activation( Wx + b )
```

Without nonlinearity, stacking linear layers is still just one linear function — the network could never learn complex patterns. The activation function (ReLU, sigmoid, tanh…) introduces the nonlinearity that lets deep networks approximate any function.

---

## 36. What's the difference between `F.relu` and `nn.ReLU`?

- **`F.relu(x)`** — a *function* (from `torch.nn.functional`). You call it directly: `y = F.relu(x)`.
- **`nn.ReLU()`** — a *module* (class). You instantiate it and use it inside `nn.Sequential`/`nn.Module`:

```python
model = nn.Sequential(nn.Linear(784, 30),
                      nn.ReLU(),       # module — has state, lives in the model
                      nn.Linear(30, 10))

# or functionally:
x = F.relu(linear(x))
```

Both compute `max(0, x)` — identical math. `nn` is the object-oriented version that fits into the `nn.Module` framework.

---

## 37. The universal approximation theorem shows that any function can be approximated as closely as needed using just one nonlinearity. So why do we normally use more?

The theorem only guarantees that a **sufficiently wide** single-hidden-layer network *can* represent any function — it says nothing about:
1. **How many neurons** you'd need (often astronomically many).
2. Whether it's **learnable/trainable** in practice.
3. **Efficiency** — deep networks represent many functions with *exponentially fewer* parameters than shallow ones.

Also, **depth helps learning**: each layer builds hierarchical features (edges → parts → objects), and deeper nets are easier to optimize and generalize better. In practice, deep + narrow beats shallow + wide.

---

**Bonus recap — the whole MNIST pipeline in one snippet:**

```python
model = nn.Linear(784, 10)                      # 1 layer: pixels → scores
dls = ImageDataLoaders.from_folder(MNIST_SAMPLE) # data, labeled by folder
learn = Learner(dls, model, loss_func=CrossEntropyLossFlat(), metrics=accuracy)
learn.fit(1)                                     # SGD: 7 steps, one epoch
```

