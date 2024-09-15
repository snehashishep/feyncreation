# LaTeX representation of particles
particle_dict = {
    'q': r'$q$', 'qbar': r'$\bar{q}$', 'qp': r"$q'$", 'qbarp': r"$\bar{q}'$",
    't': r'$t$', 'tbar': r'$\bar{t}$', 'b': r'$b$', 'bbar': r'$\bar{b}$',
    'e-': r'$e^-$', 'e+': r'$e^+$', 'mu-': r'$\mu^-$', 'mu+': r'$\mu^+$',
    'tau-': r'$\tau^-$', 'tau+': r'$\tau^+$', 've': r'$\nu_e$', 'vebar': r'$\bar{\nu_e}$',
    'vm': r'$\nu_\mu$', 'vmbar': r'$\bar{\nu_\mu}$', 'vt': r'$\nu_\tau$', 'vtbar': r'$\bar{\nu_\tau}$',
    'w+': r'$W^+$', 'w-': r'$W^-$', 'z': r'$Z$', 'gamma': r'$\gamma$', 'g': r'$g$', 'zp': r"$Z'$", 'h': r'$h$',
    'h2': r'$H^0$', 'h+': r'$H^+$', 'h-': r'$H^-$', 'h++': r'$H^{++}$', 'h--': r'$H^{--}$',
    'a0': r'$A^0$', 'del0': r'$\Delta^0$', 'del+': r'$\Delta^+$', 'del-': r'$\Delta^-$', 'del++': r'$\Delta^{++}$', 'del--': r'$\Delta^{--}$',
    'n0': r'$N^0$', 'n0bar': r'$\bar{N^0}$', 'n+': r'$N^+$', 'n-': r'$N^-$', 'n++': r'$N^{++}$', 'n--': r'$N^{--}$'
}

# Particle styles for Feynman diagrams
particle_styles = {
    # Default fermion style (straight line)
    'q': dict(), 'qbar': dict(), 'qp': dict(), 'qbarp': dict(), 
    't': dict(), 'tbar': dict(), 'b': dict(), 'bbar': dict(),
    'e-': dict(), 'e+': dict(), 'mu-': dict(), 'mu+': dict(),
    'tau-': dict(), 'tau+': dict(),
    
    # Neutrinos
    've': dict(), 'vebar': dict(), 'vm': dict(), 'vmbar': dict(), 'vt': dict(), 'vtbar': dict(),
    'n0': dict(), 'n0bar': dict(), 'n+': dict(), 'n-': dict(), 'n++': dict(), 'n--': dict(),

    'fermion': dict(),
    
    # Gluon
    'g': dict(style='linear loopy', xamp=.025, yamp=.035, nloops=7),
    
    # W and Z bosons
    'w+': dict(style='wiggly'), 'w-': dict(style='wiggly'), 'z': dict(style='wiggly'), 'gamma': dict(style='wiggly'), 'zp': dict(style='wiggly'), 'gamma': dict(style='wiggly'), 
    
    # Higgs and scalars (dashed line style)
    'h': dict(style='-', dashes=[5, 2]), 'h2': dict(style='-', dashes=[5, 2]), 'h+': dict(style='-', dashes=[5, 2]), 'h-': dict(style='-', dashes=[5, 2]),
    'h++': dict(style='-', dashes=[5, 2]), 'h--': dict(style='-', dashes=[5, 2]), 'del+': dict(style='-', dashes=[5, 2]), 'del-': dict(style='-', dashes=[5, 2]),
    'del++': dict(style='-', dashes=[5, 2]), 'del--': dict(style='-', dashes=[5, 2]), 'del0': dict(style='-', dashes=[5, 2]), 'a0': dict(style='-', dashes=[5, 2]),
}

# Particles that can have arrows
arrow_particles = ['q', 'qbar', 'qp', 'qbarp', 't', 'tbar', 'b', 'bbar', 'e-', 'e+', 'mu-', 'mu+', 
    'h+', 'h-', 'h++', 'h--', 'n+', 'n-', 'n++', 'n--', 'n0', 'n0bar', 've', 'vebar', 'vm', 'vmbar', 'vt', 'vtbar', 'del+', 'del-', 'del++', 'del--']

# Fermion list
fermion_list = ['q', 'qbar', 'qp', 'qbarp', 't', 'tbar', 'b', 'bbar', 'e-', 'e+', 'mu-', 'mu+', 
                'n+', 'n-', 'n++', 'n--', 'n0', 'n0bar', 've', 'vebar', 'vm', 'vmbar', 'vt', 'vtbar']
