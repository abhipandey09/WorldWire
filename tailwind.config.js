/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        burgundy: {
          DEFAULT: '#800020',
          dark: '#540015',
          light: '#A31936',
          deep: '#36000E'
        },
        gold: {
          DEFAULT: '#C6A15B',
          light: '#E6D29E',
          dark: '#9E7833',
          shimmer: '#FFF0C2',
          antique: '#B38B3F'
        },
        ivory: {
          DEFAULT: '#FFF8E8',
          card: '#FDF7EB',
          dark: '#EFE3CC'
        },
        champagne: {
          DEFAULT: '#F4E5C7',
          light: '#FAF1DE'
        },
        emerald: {
          DEFAULT: '#164B35',
          dark: '#0D3323',
          light: '#286E50'
        },
        rose: {
          DEFAULT: '#D98B9C',
          dark: '#B06375',
          light: '#F2C6CF'
        },
        marigold: {
          DEFAULT: '#FDB813',
          saffron: '#F58220',
          amber: '#E67E22'
        },
        night: {
          DEFAULT: '#131A26',
          dark: '#0A0E17',
          card: '#1A2333'
        }
      },
      fontFamily: {
        script: ['"Great Vibes"', 'cursive'],
        cinzel: ['"Cinzel"', 'serif'],
        cormorant: ['"Cormorant Garamond"', 'serif'],
        playfair: ['"Playfair Display"', 'serif'],
        sans: ['"Montserrat"', '"Lato"', 'sans-serif'],
      },
      boxShadow: {
        'gold-glow': '0 0 25px rgba(198, 161, 91, 0.45)',
        'gold-glow-lg': '0 0 45px rgba(198, 161, 91, 0.65)',
        'royal': '0 20px 40px -15px rgba(84, 0, 21, 0.35)',
      },
      backgroundImage: {
        'gold-gradient': 'linear-gradient(135deg, #ECC880 0%, #C6A15B 50%, #9E7833 100%)',
        'burgundy-gradient': 'linear-gradient(135deg, #540015 0%, #800020 50%, #36000E 100%)',
        'ivory-gradient': 'linear-gradient(180deg, #FFFDF8 0%, #FFF8E8 50%, #F5E8D0 100%)',
      }
    },
  },
  plugins: [],
}
