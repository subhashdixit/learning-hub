# Algorithm arithmetic checks

[Practicals](../README.md) · [Deep-learning story](../../01-theory/ALGORITHM-STORY.md)

Run `python3 verify_examples.py` with Python 3.10+; only the standard library is required. [Open the script](verify_examples.py).

Checks cover hidden-unit XOR, convolution weights, depthwise weight counts, an LSTM update, attention arithmetic, LoRA parameter count, diffusion noising, graph averaging and image patch tokens. It also verifies the forecasting chapters’ small AR, damping, component, Kalman, intermittent-demand, GARCH and combination calculations.

All assertions passed in the recorded run. These checks verify the stated calculations, not training/convergence/quality of every named architecture. For actual model fitting, use the separate forecasting comparison and the existing neural-network notebooks with their documented environments.
