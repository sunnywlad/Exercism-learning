function ordinal(listNum: number): string {
  switch(listNum % 10) {
    case 1:
      return (listNum % 100 !== 11) ? 'st' :'th'
    case 2:
      return (listNum % 100 !== 12) ? 'nd' :'th'
    case 3:
      return (listNum % 100 !== 13) ? 'rd' : 'th'
    default:
      return 'th'
  }
}

export function format(name: string, listNum: number): string {
  return `${name}, you are the ${listNum}${ordinal(listNum)} customer we serve today. Thank you!`
}
