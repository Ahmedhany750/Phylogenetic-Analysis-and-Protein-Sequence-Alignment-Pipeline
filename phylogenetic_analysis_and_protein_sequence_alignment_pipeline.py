# Install necessary libraries
!pip install biopython
!apt-get update
!apt-get install clustalo

# Write the protein sequences to a FASTA file
protein_sequences = """>protine 1_hemoglobin [Homo sapiens]
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADAL
TNAVAHVDDMPKALSALSDLHAHKLRVDPVNFK

>protine 2_myoglobin[Homo sapiens]
MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVL
TALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISECIIQVLQSKHPGDFGADAQGAMNKALELFR
KDMASNYKELGFQG

>protine 3_alpha1-antitrypsin [Homo sapiens]
MPSSVSWGILLLAGLCCLVPVSLAEDPQGDAAQKTDTSHHDQDHPTFNKITPNLAEFAFSLYRQLAHQSN
STNIFFSPVSIATAFAMLSLGTKADTHDEILEGLNFNLTEIPEAQIHEGFQELLRTLNQPDSQLQLTTGN
GLFLSEGLKLVDKFLEDVKKLYHSEAFTVNFGDTEEAKKQINDYVEKGTQGKIVDLVKELDRDTVFALVN
YIFFKGKWERPFEVKDTEEEDFHVDQVTTVKVPMMKRLGMFNIQHCKKLSSWVLLMKYLGNATAIFFLPD
EGKLQHLENELTHDIITKFLENEDRRSASLHLPKLSITGTYDLKSVLGQLGITKVFSNGADLSGVTEEAP
LKLSKAVHKAVLTIDEKGTEAAGAMFLEAIPMSIPPEVKFNKPFVFLMIEQNTKSPLFMGKVVNPTQK

>protine 4_fibrinogen alphatechinase [Homo sapiens]
MFSMRIVCLVLSVVGTAWTADSGEGDFLAEGGGVRGPRVVERHQSACKDSDWPFCSDEDWNYKCPSGCRM
KGLIDEVNQDFTNRINKLKNSLFEYQKNNKDSHSLTTNIMEILRGDFSSANNRDNTYNRVSEDLRSRIEV
LKRKVIEKVQHIQLLQKNVRAQLVDMKRLEVDIDIKIRSCRGSCSRALAREVDLKDYEDQQKQLEQVIAK
DLLPSRDRQHLPLIKMKPVPDLVPGNFKSQLQKVPPEWKALTDMPQMRMELERPGGNEITRGGSTSYGTG
SETESPRNPSSAGSWNSGSSGPGSTGNRNPGSSGTGGTATWKPGSSGPGSTGSWNSGSSGTGSTGNQNPG
SPRPGSTGTWNPGSSERGSAGHWTSESSVSGSTGQWHSESGSFRPDSPGSGNARPNNPDWGTFEEVSGNV
SPGTRREYHTEKLVTSKGDKELRTGKEKVTSGSTTTTRRSCSKTVTKTVIGPDGHKEVTKEVVTSEDGSD
CPEAMDLGTLSGIGTLDGFRHRHPDEAAFFDTASTGKTFPGFFSPMLGEFVSETESRGSESGIFTNTKES
SSHHPGIAEFPSRGKSSSYSKQFTSSTSYNRGDSTFESKSYKMADEAGSEADHEGTHSTKRGHAKSRPVR
GIHTSPLGKPSLSP

>protine 5_cytochrome c [Homo sapiens]
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLE
NPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE

>protine 6_collagen alpha-1 [Homo sapiens]
MFSFVDLRLLLLLAATALLTHGQEEGQVEGQDEDIPPITCVQNGLRYHDRDVWKPEPCRICVCDNGKVLC
DDVICDETKNCPGAEVPEGECCPVCPDGSESPTDQETTGVEGPKGDTGPRGPRGPAGPPGRDGIPGQPGL
PGPPGPPGPPGPPGLGGNFAPQLSYGYDEKSTGGISVPGPMGPSGPRGLPGPPGAPGPQGFQGPPGEPGE
PGASGPMGPRGPPGPPGKNGDDGEAGKPGRPGERGPPGPQGARGLPGTAGLPGMKGHRGFSGLDGAKGDA
GPAGPKGEPGSPGENGAPGQMGPRGLPGERGRPGAPGPAGARGNDGATGAAGPPGPTGPAGPPGFPGAVG
AKGEAGPQGPRGSEGPQGVRGEPGPPGPAGAAGPAGNPGADGQPGAKGANGAPGIAGAPGFPGARGPSGP
QGPGGPPGPKGNSGEPGAPGSKGDTGAKGEPGPVGVQGPPGPAGEEGKRGARGEPGPTGLPGPPGERGGP
GSRGFPGADGVAGPKGPAGERGSPGPAGPKGSPGEAGRPGEAGLPGAKGLTGSPGSPGPDGKTGPPGPAG
QDGRPGPPGPPGARGQAGVMGFPGPKGAAGEPGKAGERGVPGPPGAVGPAGKDGEAGAQGPPGPAGPAGE
RGEQGPAGSPGFQGLPGPAGPPGEAGKPGEQGVPGDLGAPGPSGARGERGFPGERGVQGPPGPAGPRGAN
GAPGNDGAKGDAGAPGAPGSQGAPGLQGMPGERGAAGLPGPKGDRGDAGPKGADGSPGKDGVRGLTGPIG
PPGPAGAPGDKGESGPSGPAGPTGARGAPGDRGEPGPPGPAGFAGPPGADGQPGAKGEPGDAGAKGDAGP
PGPAGPAGPPGPIGNVGAPGAKGARGSAGPPGATGFPGAAGRVGPPGPSGNAGPPGPPGPAGKEGGKGPR
GETGPAGRPGEVGPPGPPGPAGEKGSPGADGPAGAPGTPGPQGIAGQRGVVGLPGQRGERGFPGLPGPSG
EPGKQGPSGASGERGPPGPMGPPGLAGPPGESGREGAPGAEGSPGRDGSPGAKGDRGETGPAGPPGAPGA
PGAPGPVGPAGKSGDRGETGPAGPAGPVGPVGARGPAGPQGPRGDKGETGEQGDRGIKGHRGFSGLQGPP
GPPGSPGEQGPSGASGPAGPRGPPGSAGAPGKDGLNGLPGPIGPPGPRGRTGDAGPVGPPGPPGPPGPPG
PPSAGFDFSFLPQPPQEKAHDGGRYYRADDANVVRDRDLEVDTTLKSLSQQIENIRSPEGSRKNPARTCR
DLKMCHSDWKSGEYWIDPNQGCNLDAIKVFCNMETGETCVYPTQPSVAQKNWYISKNPKDKRHVWFGESM
TDGFQFEYGGQGSDPADVAIQLTFLRLMSTEASQNITYHCKNSVAYMDQQTGNLKKALLLQGSNEIEIRA
EGNSRFTYSVTVDGCTSHTGAWGKTVIEYKTTKTSRLPIIDVAPLDVGAPDQEFGFDVGPVCFL

>protine 7_Insulin [Homo sapiens]
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGG
GPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN

>protine 8_Actine [Homo sapiens]
MCDDEETTALVCDNGSGLVKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQSKRGILTLK
YPIEHGIITNWDDMEKIWHHTFYNELRVAPEEHPTLLTEAPLNPKANREKMTQIMFETFNVPAMYVAIQA
VLSLYASGRTTGIVLDSGDGVTHNVPIYEGYALPHAIMRLDLAGRDLTDYLMKILTERGYSFVTTAEREI
VRDIKEKLCYVALDFENEMATAASSSSLEKSYELPDGQVITIGNERFRCPETLFQPSFIGMESAGIHETT
YNSIMKCDIDIRKDLYANNVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILAS
LSTFQQMWISKQEYDEAGPSIVHRKCF

>protine 9_Chymotrypsine [Bovine]
ANTPDRLQQASLPLLSNTNCKKYWGTKIKDAMICAGASGVSSCMGDSGGPLVCKKNGAWTLVGIVSWGSS
TCSTSTPGVYARVTALVNWVQQTLAAN

>protine 10_trypsinogen [Homo sapiens]
MHPLLILAFVGAAVAFPSDDDDKIVGGYTCAENSVPYQVSLNAGYHFCGGSLINDQWVVSAAHCYQYHIQ
VRLGEYNIDVLEGGEQFIDASKIIRHPKYSSWTLDNDILLIKLSTPAVINARVSTLLLPSACASAGTECL
ISGWGNTLSSGVNYPDLLQCLVAPLLSHADCEASYPGQITNNMICAGFLEGGKDSCQGDSGGPVACNGQL
QGIVSWGYGCAQKGKPGVYTKVCNYVDWIQETIAANS

>protine 11_lysozyme [hen egg]
KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTP
GSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL

>protine 12_Hemoglobin betachain [Homo sapiens]
MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFLESFGDLSTPDAVMGNPKVKAHGKKVLG
AFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVAN
ALAHKYH

>protine 13_Myeloperoxidase [Homo sapiens]
MGVPFFSSLRCMVDLGPCWAGGLTAEMKLLLALAGLLAILATPQPSEGAAPAVLGEVDTSLVLSSMEEAK
QLVDKAYKERRESIKQRLRSGSASPMELLSYFKQPVAATRTAVRAADYLHVALDLLERKLRSLWRRPFNV
TDVLTPAQLNVLSKSSGCAYQDVGVTCPEQDKYRTITGMCNNRRSPTLGASNRAFVRWLPAEYEDGFSLP
YGWTPGVKRNGFPVALARAVSNEIVRFPTDQLTPDQERSLMFMQWGQLLDHDLDFTPEPAARASFVTGVN
CETSCVQQPPCFPLKIPPNDPRIKNQADCIPFFRSCPACPGSNITIRNQINALTSFVDASMVYGSEEPLA
RNLRNMSNQLGLLAVNQRFQDNGRALLPFDNLHDDPCLLTNRSARIPCFLAGDTRSSEMPELTSMHTLLL
REHNRLATELKSLNPRWDGERLYQEARKIVGAMVQIITYRDYLPLVLGPTAMRKYLPTYRSYNDSVDPRI
ANVFTNAFRYGHTLIQPFMFRLDNRYQPMEPNPRVPLSRVFFASWRVVLEGGIDPILRGLMATPAKLNRQ
NQIAVDEIRERLFEQVMRIGLDLPALNMQRSRDHGLPGYNAWRRFCGLPQPETVGQLGTVLRNLKLARKL
MEQYGTPNNIDIWMGGVSEPLKRKGRVGPLLACIIGTQFRKLRDGDRFWWENEGVFSMQQRQALAQISLP
RIICDNTGITTVSKNNIFMSNSYPRDFVNCSTLPALNLASWREAS

>protine 14_Albumin [Homo sapiens]
MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEV
TEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLV
RPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELR
DEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADD
RADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVF
LGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFE
QLGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEK
TPVSDRVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHK
PKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL

protine 15_caspase-3 [Homo sapiens]
MENTENSVDSKSIKNLEPKIIHGSESMDSGMSWDTGYKMDYPEMGLCIIINNKNFHKSTGMTSRSGTDVD
AANLRETFRNLKYEVRNKNDLTREEIVELMRDVSKEDHSKRSSFVCVLLSHGEEGIIFGTNGPVDLKKIT
NFFRGDRCRSLTGKPKLFIIQACRGTELDCGIETDSGVDDDMACHKIPVDADFLYAYSTAPGYYSWRNSK
DGSWFIQSLCAMLKQYADKLEFMHILTRVNRKVATEFESFSFDATFHAKKQIPCIVSMLTKELYFYH

>protine 16_Glyceraldehyde-3-phosphate dehydrogenase [Homo sapiens]
MGKVKVGVNGFGRIGRLVTRAAFNSGKVDIVAINDPFIDLNYMVYMFQYDSTHGKFHGTVKAENGKLVIN
GNPITIFQERDPSKIKWGDAGAEYVVESTGVFTTMEKAGAHLQGGAKRVIISAPSADAPMFVMGVNHEKY
DNSLKIISNASCTTNCLAPLAKVIHDNFGIVEGLMTTVHAITATQKTVDGPSGKLWRDGRGALQNIIPAS
TGAAKAVGKVIPELNGKLTGMAFRVPTANVSVVDLTCRLEKPAKYDDIKKVVKQASEGPLKGILGYTEHQ
VVSSDFNSDTHSSTFDAGAGIALNDHFVKLISWYDNEFGYSNRVVDLMAHMASKE

>protine 17_Carbonic anhydrase [Homo sapiens]
MPRRSLHAAAVLLLVILKEQPSSPAPVNGSKWTYFGPDGENSWSKKYPSCGGLLQSPIDLHSDILQYDAS
LTPLEFQGYNLSANKQFLLTNNGHSVKLNLPSDMHIQGLQSRYSATQLHLHWGNPNDPHGSEHTVSGQHF
AAELHIVHYNSDLYPDASTASNKSEGLAVLAVLIEMGSFNPSYDKIFSHLQHVKYKGQEAFVPGFNIEEL
LPERTAEYYRYRGSLTTPPCNPTVLWTVFRNPVQISQEQLLALETALYCTHMDDPSPREMINNFRQVQKF
DERLVYTSFSQVQVCTAAGLSLGIILSLALAGILGICIVVVVSIWLFRRKSIKKGDNKGVIYKPATKMET

>protine 18_cytoglobin [Homo sapiens]
MEKVPGEMEIERRERSEELSEAERKAVQAMWARLYANCEDVGVAILVRFFVNFPSAKQYFSQFKHMEDPL
EMERSPQLRKHACRVMGALNTVVENLHDPDKVSSVLALVGKAHALKHKVEPVYFKILSGVILEVVAEEFA
SDFPPETQRAWAKLRGLIYSHVTAAYKEVGWVQQVPNATTPPATLPSSGP

>protine 19_Troponin C [Homo sapiens]
MTDQQAEARSYLSEEMIAEFKAAFDMFDADGGGDISVKELGTVMRMLGQTPTKEELDAIIEEVDEDGSGT
IDFEEFLVMMVRQMKEDAKGKSEEELAECFRIFDRNADGYIDPGELAEIFRASGEHVTDEEIESLMKDGD
KNNDGRIDFDEFLKMMEGVQ

>protine 20_Kallikrein [Homo sapiens]
MWFLVLCLALSLGGTGAAPPIQSRIVGGWECEQHSQPWQAALYHFSTFQCGGILVHRQWVLTAAHCISDN
YQLWLGRHNLFDDENTAQFVHVSESFPHPGFNMSLLENHTRQADEDYSHDLMLLRLTEPADTITDAVKVV
ELPTQEPEVGSTCLASGWGSIEPENFSFPDDLQCVDLKILPNDECEKAHVQKVTDFMLCVGHLEGGKDTC
VGDSGGPLMCDGVLQGVTSWGYVPCGTPNKPSVAVRVLSYVKWIEDTIAENS


"""

# Save the sequences to a file
with open("sequences.fasta", "w") as file:
    file.write(protein_sequences)

# Align the sequences using Clustal Omega
from Bio.Align.Applications import ClustalOmegaCommandline

clustalomega_cline = ClustalOmegaCommandline(
    infile="sequences.fasta",
    outfile="aligned.fasta",
    verbose=True,
    auto=True,
    force=True  # Force overwrite if the output file exists
)
clustalomega_cline()

# Read the aligned sequences and ensure unique IDs
from Bio import AlignIO

alignment = AlignIO.read("aligned.fasta", "fasta")

# Check for duplicate IDs and make them unique
seen_ids = set()
for i, record in enumerate(alignment):
    if record.id in seen_ids:
        record.id = f"{record.id}_{i}"  # Append an index to make it unique
    seen_ids.add(record.id)

# Calculate the distance matrix
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)
print(distance_matrix)

# Build the UPGMA tree
constructor = DistanceTreeConstructor()
upgma_tree = constructor.upgma(distance_matrix)

# Function to assign custom labels to internal nodes
def label_internal_nodes(tree):
    counter = 1
    for clade in tree.find_clades():
        if clade.name is None:
            clade.name = f"Node{counter}"
            counter += 1

# Label the internal nodes
label_internal_nodes(upgma_tree)

# Enhanced Visualization for UPGMA Tree with Custom Labels
import matplotlib.pyplot as plt
from Bio import Phylo

print("UPGMA Tree:")
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(1, 1, 1)
Phylo.draw(upgma_tree, do_show=False, axes=ax)
plt.title("UPGMA Tree of Protein Sequences with Node Labels", fontsize=16, fontweight="bold")
plt.xlabel("Branch Length", fontsize=12)
plt.ylabel("Taxa", fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(color="gray", linestyle="--", linewidth=0.5)
plt.savefig("upgma_tree_custom_labels.png", dpi=300, bbox_inches="tight")
plt.show()

# Print the tree with labels in ASCII format
Phylo.draw_ascii(upgma_tree)

# Build the Neighbor Joining (NJ) tree
nj_tree = constructor.nj(distance_matrix)

# Enhanced Visualization for NJ Tree
print("Neighbor Joining Tree:")
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(1, 1, 1)
Phylo.draw(nj_tree, do_show=False, axes=ax)
plt.title("Neighbor Joining Tree of Protein Sequences", fontsize=16, fontweight="bold")
plt.xlabel("Branch Length", fontsize=12)
plt.ylabel("Taxa", fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(color="gray", linestyle="--", linewidth=0.5)
plt.savefig("nj_tree_stylized.png", dpi=300, bbox_inches="tight")
plt.show()

# Save the trees in Newick format
Phylo.write(upgma_tree, "upgma_tree.nwk", "newick")
Phylo.write(nj_tree, "nj_tree.nwk", "newick")
