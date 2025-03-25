
const getCustomer = async () => {
  const resp = await fetch(`https://telco.axiom-hasura.private-ddn.hasura.app/v1/rest/auth/Users?page%5Blimit%5D=10&page%5Boffset%5D=0&fields%5BUsers%5D=email%2Cid`);
  const data = await resp.json();
  console.log(`data: ${JSON.stringify(data)}`)
};


const main = async () => {
  await getCustomer();
}


main()