
//  la progression dynamique
let totalTaches = {{ taches|length }};
let tachesCompletees = {{ taches|selectattr('complete', 'eq', True)|length }};
let barreProgression = document.querySelector(".progres-bar svg rect:nth-child(2)");

if (totalTaches > 0) {
    let progression = (tachesCompletees / totalTaches) * 320; // 320 est la largeur maximale
    barreProgression.setAttribute("width", progression);
}
