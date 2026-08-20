# -*- coding: utf-8 -*-
"""
===============================================================================
 MNIST BASICS: nn.Linear  +  Cross Entropy  (A Gentle Introduction)
===============================================================================

This file teaches the two most important building blocks of a neural network
for classification (like MNIST handwritten digit recognition):

    1.  nn.Linear  -- the "fully connected" layer that does the math
    2.  CrossEntropyLoss -- the "scoreboard" that tells us how wrong we are

Everything is explained with:
    • plain-English intuition
    • math formulas  (written in LaTeX-style in comments so you can paste them
      into a Markdown/Notebook cell and they will render beautifully)
    • small, runnable Python / PyTorch code

Run this file directly:
    python mnist-basics.py

(You'll need:  pip install torch)
===============================================================================
"""


# =============================================================================
#  PART 0 — THE BIG PICTURE
# =============================================================================
#
# Imagine the MNIST problem: 28x28 grayscale images of handwritten digits.
#
#   - Each image is just a list of 28 * 28 = 784 numbers (pixel intensities).
#   - Each image belongs to 1 of 10 classes: digit 0, digit 1, ..., digit 9.
#
# A neural net for this looks like:
#
#           784 pixels  --->  [ nn.Linear(784, 10) ]  --->  10 scores
#
# So in one line:
#     nn.Linear(784, 10)
#
#   -> takes 784 numbers in
#   -> outputs 10 numbers  (one "score" per digit)
#
# Then Cross Entropy turns those 10 scores into ONE number:
#     "how wrong were we?"
#
# Gradient descent (optimizer) then tweaks the weights so that number gets
# smaller and smaller.  That's the whole game.  Let's unpack each piece.
# =============================================================================


# =============================================================================
#  PART 1 — nn.Linear  (the math of a fully connected layer)
# =============================================================================
#
# ---------------------------------------------------------------------------
# 1.1  Intuition
# ---------------------------------------------------------------------------
# A Linear layer is just a big "weighted vote" machine.
#
#   - Each input value x_i gets multiplied by a weight w_i.
#   - All the weighted values are summed up.
#   - A bias b is added.
#   - The result is one output "score".
#
# If you've seen linear regression, this is EXACTLY the same idea, but we
# build many of these in parallel (one per output neuron).
#
# ---------------------------------------------------------------------------
# 1.2  The math — one output neuron
# ---------------------------------------------------------------------------
#
# For a single neuron with n inputs:
#
#         z  =  w_1 x_1  +  w_2 x_2  +  ...  +  w_n x_n  +  b
#
#              z  =  Σ_{i=1}^{n} w_i x_i  +  b
#
# Or in vector form (the way PyTorch actually computes it):
#
#         z  =  Wᵀ x  +  b
#
#   where:
#         x  ∈ Rⁿ        input vector        (the 784 pixels)
#         W  ∈ Rⁿ        weight vector
#         b  ∈ R         bias  (a scalar)
#         z  ∈ R         the output score
#
# ---------------------------------------------------------------------------
# 1.3  The math — a whole layer with k output neurons
# ---------------------------------------------------------------------------
#
# If we want k outputs (e.g. k = 10 for 10 digits) we stack k of these.
# Now W becomes a MATRIX of shape (k, n):
#
#         z  =  W x  +  b
#
#   where:
#         x  ∈ Rⁿ            input vector
#         W  ∈ R^{k × n}     weight matrix     <-- PyTorch stores this as (out, in)
#         b  ∈ R^k           bias vector
#         z  ∈ R^k           output scores
#
# Written out fully:
#
#         ┌ z_0 ┐     ┌ w_00  w_01  ...  w_0,n-1 ┐   ┌ x_0 ┐   ┌ b_0 ┐
#         │ z_1 │  =  │ w_10  w_11  ...  w_1,n-1 │   │ x_1 │   │ b_1 │
#         │ ... │     │  ...   ...  ...   ...     │ · │ ... │ + │ ... │
#         └ z_9 ┘     └ w_90  w_91  ...  w_9,n-1 ┘   └ x_9 ┘   └ b_9 ┘
#
# ---------------------------------------------------------------------------
# 1.4  PyTorch convention
# ---------------------------------------------------------------------------
#
#     nn.Linear(in_features, out_features)
#
# The weight matrix has shape:  (out_features, in_features)
# The bias vector has shape:    (out_features,)
#
# IMPORTANT: The weight matrix is stored TRANSPOSED relative to the textbook
# math.  PyTorch computes:   z = x @ Wᵀ + b
#
#   (in_features, out_features)   @   (out_features, in_features)ᵀ
#                 = (out_features,)
#
# ---------------------------------------------------------------------------
# 1.5  Where do the weights come from?
# ---------------------------------------------------------------------------
# Initially random (PyTorch picks smart small values).  Then the optimizer
# (gradient descent) adjusts W and b so the loss (Part 2) gets smaller.
# =============================================================================


# =============================================================================
#  PART 2 — CROSS ENTROPY  (the loss function for classification)
# =============================================================================
#
# ---------------------------------------------------------------------------
# 2.1  Intuition
# ---------------------------------------------------------------------------
# Cross entropy answers:  "How surprised are we by the true answer?"
#
#   - The model outputs raw scores (logits).
#   - We convert them into probabilities (0..1, summing to 1) with softmax.
#   - If the model puts HIGH probability on the correct class  -> small loss.
#   - If the model puts LOW  probability on the correct class  -> huge loss.
#
# It is the standard loss for multi-class classification (MNIST included).
#
# ---------------------------------------------------------------------------
# 2.2  Step 1 — Softmax (turn scores into probabilities)
# ---------------------------------------------------------------------------
#
# Given raw scores (logits)  z_0, z_1, ..., z_{k-1}:
#
#                    exp(z_j)
#         p_j  =  ──────────────────
#                  Σ_{i=0}^{k-1} exp(z_i)
#
#   where:
#         exp(z) = e^z        (e ≈ 2.71828)
#         p_j                = predicted probability of class j
#
# This guarantees:
#         p_j ∈ (0, 1)     and     Σ_j p_j = 1
#
# (The exp makes scores positive, then we normalize so they sum to 1.)
#
# ---------------------------------------------------------------------------
# 2.3  Step 2 — The Cross Entropy formula
# ---------------------------------------------------------------------------
#
# For one sample with true label y (a class index) and predicted
# probabilities p_0, ..., p_{k-1}:
#
#         L  =  - log( p_y )
#
#   i.e. only look at the probability the model gave to the CORRECT class.
#
#   - Perfect prediction (p_y = 1)  ->  L = -log(1) = 0   (no pain)
#   - Bad prediction    (p_y → 0)  ->  L → +∞            (lots of pain)
#
# A mathematically equivalent form (using one-hot labels y_j) is:
#
#         L  =  - Σ_{j=0}^{k-1} y_j · log( p_j )
#
#   where y_j = 1 if j is the true class, else 0.
#   (This form is what the name "cross entropy" refers to — the log only
#    "fires" for the true class because all other y_j are zero.)
#
# ---------------------------------------------------------------------------
# 2.4  The full formula, end to end (softmax + cross entropy combined)
# ---------------------------------------------------------------------------
#
# Plug softmax into cross entropy.  For true class y:
#
#                                  exp( z_y )
#         L  =  - log( p_y )  =  - log( ────────────────── )
#                                      Σ_{i=0}^{k-1} exp(z_i)
#
# Use the log rule  log(a/b) = log a - log b:
#
#         L  =  - z_y  +  log( Σ_{i=0}^{k-1} exp(z_i) )
#
# This combined form is EXACTLY what PyTorch computes in one shot — it is
# numerically more stable than doing softmax then log separately.
#
# ---------------------------------------------------------------------------
# 2.5  Batching (what PyTorch actually does)
# ---------------------------------------------------------------------------
#
# For a batch of N samples, the loss is the AVERAGE over all samples:
#
#                  1    N
#         L_batch  =  ─ · Σ  L_m
#                  N   m=1
#
# That single number is what we call "the loss" — and it's the number the
# optimizer minimizes.
#
# ---------------------------------------------------------------------------
# 2.6  PyTorch: two ways, same result
# ---------------------------------------------------------------------------
#
#   Way 1 (recommended, numerically stable):
#       loss = F.cross_entropy(logits, targets)
#         -> expects RAW scores (logits), NOT probabilities
#         -> combines softmax + log + negative-log-likelihood internally
#
#   Way 2 (for learning only, less stable):
#       probs = F.softmax(logits, dim=1)
#       loss  = F.nll_loss(torch.log(probs), targets)
#
# Both give (nearly) the same number.  Always use Way 1 in practice.
# =============================================================================


# =============================================================================
#  PART 3 — CODE: build the two pieces and watch them work
# =============================================================================

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(42)  # reproducible results


# -----------------------------------------------------------------------------
# 3.1  Build the Linear layer for MNIST
# -----------------------------------------------------------------------------
# in_features  = 784  (28 x 28 pixels flattened)
# out_features = 10   (scores for digits 0..9)
# -----------------------------------------------------------------------------

layer = nn.Linear(in_features=784, out_features=10)

print("=" * 70)
print("nn.Linear(784, 10)")
print("=" * 70)
print(f"Weight matrix shape (out, in): {layer.weight.shape}")
print(f"Bias vector shape        (out,): {layer.bias.shape}")
print()

# Let's fake ONE MNIST image: 784 random pixel values in [0, 1].
x = torch.rand(784)  # shape (784,)

z = layer(x)  # forward pass:  z = x @ Wᵀ + b
print(f"Input  x  shape: {tuple(x.shape)}  (28 x 28 = 784 pixels, flattened)")
print(f"Output z shape:  {tuple(z.shape)}  (10 raw scores, one per digit)")
print(f"Raw scores (logits): {z.detach().numpy()}")
print()


# -----------------------------------------------------------------------------
# 3.2  Manual implementation of the SAME math (no autograd tricks)
# -----------------------------------------------------------------------------
# Recall:  z_j = Σ_i W[j, i] * x[i] + b[j]
# -----------------------------------------------------------------------------

def linear_manual(x, weight, bias):
    """Pure-Python/NumPy-style implementation of nn.Linear.

    weight has shape (out, in), bias has shape (out,).
    """
    out_features, in_features = weight.shape
    z = torch.zeros(out_features)
    for j in range(out_features):                     # for each output neuron
        total = bias[j]
        for i in range(in_features):                  # sum of weighted inputs
            total += weight[j, i] * x[i]
        z[j] = total
    return z


z_manual = linear_manual(x, layer.weight.detach(), layer.bias.detach())
z_pytorch = layer(x).detach()

print("-" * 70)
print("Sanity check: manual math == PyTorch?")
print("-" * 70)
print(f"Max |difference| = {(z_manual - z_pytorch).abs().max().item():.2e}")
print()


# -----------------------------------------------------------------------------
# 3.3  Cross Entropy by hand
# -----------------------------------------------------------------------------

# Suppose the TRUE label for this image is digit 3.
y_true = 3

# --- Step 1: softmax -----------------------------------------------
def softmax(logits):
    exp_logits = torch.exp(logits - logits.max())  # subtract max for stability
    return exp_logits / exp_logits.sum()


p = softmax(z_pytorch)

print("-" * 70)
print("Softmax: raw scores -> probabilities")
print("-" * 70)
for j, prob in enumerate(p):
    marker = "  <-- TRUE label" if j == y_true else ""
    print(f"  digit {j}:  p = {prob.item():.4f}{marker}")
print(f"  sum of all p = {p.sum().item():.4f}  (must be 1)")
print()

# --- Step 2: cross entropy for ONE sample ---------------------------
#   L = -log(p_y)
loss_one = -torch.log(p[y_true])

print("-" * 70)
print("Cross entropy (single sample)")
print("-" * 70)
print(f"  L = -log(p_{y_true}) = -log({p[y_true].item():.4f}) = {loss_one.item():.4f}")
print()

# --- Equivalent: PyTorch's one-shot F.cross_entropy -----------------
# Note: cross_entropy takes RAW logits, not probabilities!
loss_pytorch = F.cross_entropy(z_pytorch.unsqueeze(0), torch.tensor([y_true]))

print(f"  F.cross_entropy(logits, target) = {loss_pytorch.item():.4f}")
print()


# -----------------------------------------------------------------------------
# 3.4  Why a "confident wrong" answer explodes the loss
# -----------------------------------------------------------------------------
# Build a tiny demo: probability given to the correct class vs. the loss.
# -----------------------------------------------------------------------------

print("-" * 70)
print("Loss vs. probability of the correct class")
print("-" * 70)
print(f"  {'p_correct':>10} | {'loss = -log(p)':>16}")
print("  " + "-" * 30)
for pc in [0.99, 0.90, 0.50, 0.10, 0.01]:
    loss = -math.log(pc)
    print(f"  {pc:>10.2f} | {loss:>16.4f}")

print()
print("=> The worse the model is (small p_correct), the bigger the loss.")
print("=> Gradient descent will push the weights to make p_correct grow.")
print()


# -----------------------------------------------------------------------------
# 3.5  A full 1-step "training" loop skeleton (the MNIST pattern)
# -----------------------------------------------------------------------------
# This is the exact template you'll use for real MNIST training.  The key
# ingredients:  a Linear layer, Cross Entropy loss, and an optimizer.
# -----------------------------------------------------------------------------

def one_training_step():
    # (Pretend) batch of 64 images, each 784 pixels.
    xs = torch.randn(64, 784)
    # (Pretend) true labels for each image in the batch.
    ys = torch.randint(0, 10, (64,))

    model = nn.Linear(784, 10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # Forward pass: raw scores for the whole batch.
    logits = model(xs)                      # shape (64, 10)

    # The one line that matters: softmax + log + NLL combined.
    loss = F.cross_entropy(logits, ys)      # scalar: average over the batch

    # Backward pass: compute gradients of the loss w.r.t. W and b.
    optimizer.zero_grad()
    loss.backward()

    # Update: W <- W - lr * dL/dW ,  b <- b - lr * dL/db
    optimizer.step()

    return loss.item()


loss_before = one_training_step()
# (We only do 1 step here; in real training you'd loop over the whole dataset
#  many times.  Each pass lowers the loss a little.)

print("-" * 70)
print("Result of one SGD step on a random batch:")
print("-" * 70)
print(f"  loss = {loss_before:.4f}   (a random-start loss, ~2.30 = -log(0.1))")
print()
print("  Note: with 10 classes, random guessing gives p = 0.1 per class,")
print("        so  L = -log(0.1) ≈ 2.3026.  Our loss is right in that range.")
print()


# =============================================================================
#  PART 4 — CHEAT SHEET (recap)
# =============================================================================
#
#  ┌───────────────────────────────────────────────────────────────────────┐
#  │  nn.Linear(in, out)                                                   │
#  │                                                                       │
#  │     z  =  x @ Wᵀ  +  b                                                │
#  │     W shape: (out, in)    b shape: (out,)                             │
#  │     x shape: (batch, in)  z shape: (batch, out)                       │
#  │                                                                       │
#  │  CrossEntropyLoss (via F.cross_entropy)                               │
#  │                                                                       │
#  │     L  =  - z_y  +  log( Σ_i exp(z_i) )          (one sample)         │
#  │     L_batch  =  average over all samples in the batch                 │
#  │                                                                       │
#  │  Pipeline:  logits -> softmax -> -log(p_true)  =  the loss            │
#  └───────────────────────────────────────────────────────────────────────┘
#
# That's it!  Linear layers transform the input, Cross Entropy scores how
# wrong we are, and gradient descent updates the weights to reduce that score.
# =============================================================================

