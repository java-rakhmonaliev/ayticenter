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
        display: ['"Archivo"', 'system-ui', 'sans-serif'],
        sans: ['"Archivo"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      colors: {
        nb: {
          base:     '#070908',
          surface:  '#0C110E',
          elevated: '#0E1410',
          footer:   '#0A0D0B',
        },
        accent: {
          DEFAULT: '#2BE57B',
          dim:     'rgba(43,229,123,0.12)',
          glow:    'rgba(43,229,123,0.35)',
        },
        hot: {
          DEFAULT: '#E8302A',
          text:    '#FF6B5E',
        },
        border: {
          DEFAULT: 'rgba(255,255,255,0.08)',
          bright:  'rgba(255,255,255,0.16)',
        },
        text: {
          primary:   '#F2F4F0',
          secondary: 'rgba(242,244,240,0.55)',
          tertiary:  'rgba(242,244,240,0.35)',
        },
      },
      borderRadius: {
        'nb-sm': '11px',
        'nb-md': '15px',
        'nb-lg': '18px',
        'nb-xl': '22px',
      },
      transitionTimingFunction: {
        'spring':   'cubic-bezier(0.34, 1.56, 0.64, 1)',
        'out-expo': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
    },
  },
  plugins: [],
};
