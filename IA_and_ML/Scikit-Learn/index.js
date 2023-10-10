const fs = require("fs/promises");

(async () => {
  const file = (await fs.readFile(__dirname + "/nfs-selected.json")).toString();

  const newFile = JSON.parse(file);

  const formatted = Array.from(
    { length: Number(newFile.at(-1).num_nf) - Number(newFile[0].num_nf) },
    (_, i) =>
      i
        ? newFile.find(
            (e) => Number(e.num_nf) === Number(newFile[i - 1]?.num_nf) + 1
          ) || {
            ...newFile[i - 1],
            num_nf: `${Number(newFile[i - 1]?.num_nf) + 1}`.padStart(9, "0"),
            cod_nf: "undefined",
          }
        : newFile[i]
  );

  await fs.writeFile(
    __dirname + "/new-formatted-nfs.json",
    JSON.stringify(formatted, null, 2)
  );
})();
