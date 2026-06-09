/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js",
    "./**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Syne"', 'system-ui', 'sans-serif'],
        sans: ['"DM Sans"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      colors: {
        nb: {
          base:     '#0A0A0C',
          surface:  '#111114',
          elevated: '#18181C',
          glass:    'rgba(255,255,255,0.03)',
        },
        accent: {
          DEFAULT: '#FF5C1A',
          dim:     'rgba(255,92,26,0.15)',
          glow:    'rgba(255,92,26,0.25)',
        },
        border: {
          DEFAULT: 'rgba(255,255,255,0.07)',
          bright:  'rgba(255,255,255,0.14)',
        },
        text: {
          primary:   '#F0EFE8',
          secondary: 'rgba(240,239,232,0.55)',
          tertiary:  'rgba(240,239,232,0.28)',
        },
      },
      fontSize: {
        'display-xl': ['clamp(4rem,10vw,9rem)',   { lineHeight: '0.95', letterSpacing: '-0.03em' }],
        'display-lg': ['clamp(3rem,7vw,6.5rem)',  { lineHeight: '1.0',  letterSpacing: '-0.028em' }],
        'display-md': ['clamp(2rem,4.5vw,3.5rem)',{ lineHeight: '1.1',  letterSpacing: '-0.02em' }],
        'display-sm': ['clamp(1.5rem,3vw,2.25rem)',{ lineHeight: '1.15', letterSpacing: '-0.018em' }],
        'mono-label': ['0.6875rem', { lineHeight: '1.4', letterSpacing: '0.1em' }],
      },
      borderRadius: {
        'nb-sm': '8px',
        'nb-md': '16px',
        'nb-lg': '24px',
      },
      transitionTimingFunction: {
        'spring':   'cubic-bezier(0.34, 1.56, 0.64, 1)',
        'out-expo': 'cubic-bezier(0.22, 1, 0.36, 1)',
        'in-expo':  'cubic-bezier(0.64, 0, 0.78, 0)',
      },
      spacing: {
        'section':    '9rem',
        'section-sm': '6rem',
      },
      boxShadow: {
        'nb-sm':  '0 2px 8px rgba(0,0,0,0.5)',
        'nb-md':  '0 8px 32px rgba(0,0,0,0.6)',
        'nb-lg':  '0 24px 64px rgba(0,0,0,0.7)',
        'glow':   '0 0 40px rgba(255,92,26,0.25)',
        'glow-lg':'0 0 80px rgba(255,92,26,0.15)',
      },
    },
  },
  plugins: [],
};
