<script lang="ts">
  import NavBar from "../../Components/NavBar.svelte";
  import InfoText from "../../Components/InfoText.svelte";
  import TopicA from '../../../assets/Committees/GA/Topic1.jpg';
  import TopicB from '../../../assets/Committees/GA/Topic2.jpg'

</script>

<NavBar />

<h1 class="text-center font-bold underline text-6xl my-10"> General Assembly </h1>
<div class="grid grid-flow-row mx-auto space-y-8">
  <InfoText 
    image={TopicA}
    title="Topic 1: The Question of Whether Social and Security Concerns Call for Niqab Baba and Regulation"
    paragraphB=""
    paragraphA="The issue of whether social and security concerns call for niqab bans and regulations
    has been increasingly brought into the spotlight in recent years. Some countries, such as
    France and Belgium, have placed certain bans and regulations for the niqab and other face
    coverings, while others still allow it as a form of freedom and religious expression. This has
    raised a number of complex ethical, legal, social, and security questions."
    link="https://drive.google.com/file/d/1iVrRiQZTnYRWFAETbo3n_43Ftrqlv7dA/view?usp=sharing"
    />

  <InfoText 
    image={TopicB} 
    title="Topic 2: Developing Internal Frameworks to Combat Animal Cruelty and Unethical Practices in Slaughterhouses and Fashion Industries"
    paragraphB="
    This not only raises ethical concerns but also poses serious questions about the sustainability
    and morality of our food production system. As we delve into the complexities of animal
    cruelty in both sectors, it becomes increasingly evident that urgent action is needed to
    address these systemic issues and ensure the well-being of both industry workers and the
    animals involved."
    paragraphA="The exploitation of animals in slaughterhouses and the fashion industry has long
    been a contentious issue with far-reaching consequences. Historically, animals have been
    utilized in the clothing industry for their hides, fur, and other materials, leading to the
    proliferation of unethical practices in the pursuit of profit. This exploitation experienced a
    significant boom during periods of industrialization and globalization, as demand for
    affordable clothing surged. However, this expansion came at the expense of animal welfare,
    with inhumane treatment and poor handling becoming commonplace in slaughterhouses."
    link="https://drive.google.com/file/d/1Lf1ekdt10Jc4dutXXaw4ylFpeNpOC2rA/view?usp=sharing"
    />
</div>

