# FeynCreation

**FeynCreation** is a Python tool that allows you to generate Feynman diagrams interactively, using the `feynman` package.

## Features

- Currently has four classes of diagrams: `decay` for 1 -> 2 processes, `twotwo` that handles 2->2 processes, `vbf1` that has VBF-type production of single particles, and `vbf2` with VBF-type pair production.
- Has four-point contact annihilation, s-channel, and t-channel diagrams for `twotwo` and `vbf2` processes.
- Has2 2-body, 3-body, and triangle diagrams for the `decay` processes.
- Uses LaTeX to render particle labels in diagrams.
- Supports customizable arrows for incoming, outgoing, and mediator particles.
- Supports interactive, card-based, and script-based generation.
- Own particles and their latex rendering can be added manually in the `particles.py` file.

## Requirements

For plotting and drawing, one requires `matplotlib` and `feynman` packages. They are already included in the `setup.py` so no need to install them separately.

Some Ubuntu computers show an error in rendering the LaTeX labels due to the absence of the `cm-super` package. This is the fix for that:
```bash
sudo apt install cm-super
```

## Installation

Clone the repository and install the package:

```bash
git clone git@github.com:snehashishep/feyncreation.git
cd feyncreation
pip install -e .
```

## Usage

from the package directory, in the command line, type and enter:

```bash
feyncreation
```

and follow the prompts.

- If you want to use an input card, type `yes` when prompted. Card file examples are in `examples/*_input.txt`.
- Type relative path to the card file in the prompt.
- If not using card file, choose the process class: currently we have `decay`, `twotwo`, `vbf1`, `vbf2`.
- For `twotwo` or `vbf2`, choose `four-point`, `s-channel` or `t-channel` at the next prompt. For `decay` choose from `2-body`, `3-body`, and `triangle`.
- Enter the basic process, like `q qbar > t tbar` for `twotwo`, `q qbar > q qbar h` for `vbf1`, `q qbar > q qbar h h` for `vbf2`.
- For `2-body` and `triangle` decays, input follows the `in > out1 out2` format, while for `3-body`, it is `in > out1 out2 out3`.
- Follow the rest of the prompts accordingly. When prompted with arrow requirement for incoming/outgoing/vector boson particles, enter the particle names separated by space.
- Lastly, enter the `filename` so that your file will be saved as `filename.png`.

For script-based usage, see `examples/*_script.py` files. Simply run the script like:

```bash
python3 examples/*_script.py
```

## Example Diagrams

### Pseudoscalar DM annihilation (`twotwo.four-point`)
<img src="examples/dm_annihilation.png" alt="four-point" width="200"/>

### $hZ$ production from $e^+ e^-$ collision (`twotwo.s-channel`)
<img src="examples/ee_hz_schannel.png" alt="s-channel" width="200"/>

### $t$-channel $q\bar{q}\to t\bar{t}$ (`twotwo.t-channel`)
<img src="examples/qq_tt_tchannel.png" alt="t-channel" width="200"/>

### VBF production of charged Scalar from $\mu^+ \mu^-$ collision (`vbf1`)
<img src="examples/vbf_mupmun_munuhp.png" alt="VBF" width="200"/>

### $gg \to t\bar{t}h$ production, looks like VBF (`vbf1`)
<img src="examples/gg_tth.png" alt="VBFlike" width="200"/> 

### $\mu^+ \mu^- \to \mu^+ \nu_\mu H^- H^0$ production, VBF with a $t$-channel mediator (`vbf2.t-channel`)
<img src="examples/vbf_hph0_mucol.png" alt="VBF2" width="200"/> 

### $H^+ \to Z W^+$ decay (`decay.2-body`)
<img src="examples/hpzw.png" alt="VBFlike" width="200"/> 

### $N^+ \to N^0 e^+ \nu_e$ decay via off-shell $W^+$ boson (`decay.3-body`)
<img src="examples/npdecay.png" alt="VBFlike" width="200"/>

### $h \to \gamma \gamma$ decay via top-quark loop (`decay.triangle`)
<img src="examples/haa-tloop.png" alt="VBFlike" width="200"/>  
