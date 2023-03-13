// https://capturetheflag.withgoogle.com/beginners-quest
// challenge 3
// https://high-speed-chase-web.2021.ctfcompetition.com/
function controlCar(scanArray){
  const check = (a,b,c) => {
    if (a==b && a==c && b==c && b!=0) {
      return true
    }
    return false
  }

  let max = scanArray[0]//Number.MIN_VALUE
  let index = 0
  for(let i=1; i< scanArray.length-1; i++){
    const a = scanArray[i-1]
    const b = scanArray[i]
    const c = scanArray[i+1]
    if(check(a, b, c)){
      if(b >= max || (b < 0 && b > -0.25)){
        max=b
        index=i
      }
    } else {
      if (a==b && i-1!=index){
        if(b >= max || (b < 0 && b > -0.25)){
          max=b
          index=i
        }
      }
    }
  }
  console.log(index, scanArray)
  if(index < 8) {
    return -1
  }

  if(index > 8) {
    return 1
  }

  return 0
}

