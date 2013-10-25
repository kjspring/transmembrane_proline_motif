/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Pierre Lindenbaum
 */
import java.io.InputStream;
import java.net.URL;
import java.util.zip.GZIPInputStream;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Unmarshaller;
import javax.xml.namespace.QName;
import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.events.XMLEvent;
import org.uniprot.uniprot.Entry;
import org.uniprot.uniprot.FeatureType;
import org.uniprot.uniprot.LocationType;
import org.uniprot.uniprot.PositionType;

/* xjc "http://www.uniprot.org/support/docs/uniprot.xsd" */
public class Biostar5862
    {
    private String description=null;
    private String type=null;

    private void run() throws Exception
        {
        JAXBContext jc = JAXBContext.newInstance("org.uniprot.uniprot");
        Unmarshaller decoder=jc.createUnmarshaller();

        URL url=new URL("ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz");
        InputStream in=new GZIPInputStream(url.openStream());
        XMLInputFactory factory = XMLInputFactory.newInstance();
        factory.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, Boolean.TRUE);
        factory.setProperty(XMLInputFactory.IS_VALIDATING, Boolean.FALSE);
        factory.setProperty(XMLInputFactory.IS_COALESCING, Boolean.TRUE);
        factory.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES, Boolean.FALSE);
        XMLEventReader r= factory.createXMLEventReader(in);
        while(r.hasNext())
            {
            XMLEvent evt=r.peek();
            if(!evt.isStartElement()) { r.next(); continue;}
            QName qName=evt.asStartElement().getName();
            if(!qName.getLocalPart().equals("entry"))  { r.next(); continue;}

            Entry entry= decoder.unmarshal(r,Entry.class).getValue();

            for(FeatureType featureType:entry.getFeature())
                {
                boolean ok=false;
                if(this.description!=null &&
                        this.description.equalsIgnoreCase(featureType.getDescription()))
                    {
                    ok=true;
                    }
                if(this.type!=null &&
                        this.type.equalsIgnoreCase(featureType.getType()))
                    {
                    ok=true;
                    }
                if(!ok) continue;
                LocationType locType=featureType.getLocation();
                if(locType==null) continue;
                PositionType begin=locType.getBegin();
                PositionType end=locType.getEnd();
                PositionType pos=locType.getPosition();
                if(pos!=null)
                    {
                    int n=pos.getPosition().intValue()-1;
                    System.out.println(">"+entry.getName()+"|"+pos.getPosition());
                    System.out.println(entry.getSequence().getValue().substring(n-1,n));
                    }
                else if(end!=null && begin!=null)
                    {
                    int n1=begin.getPosition().intValue()-1;
                    int n2=end.getPosition().intValue()-1;
                    System.out.println(">"+entry.getName()+"|"+begin.getPosition()+"-"+end.getPosition());
                    System.out.println(entry.getSequence().getValue().substring(n1,n2+1));
                    }
                }
            }
        r.close();
        in.close();
        }

    public static void main(String[] args)
        {
        try {
            Biostar5862 app=new Biostar5862();
            int optind=0;
            while(optind<args.length)
                {
                if(args[optind].equals("-h"))
                    {
                    return;
                    }
                else if(args[optind].equals("-d"))
                    {
                    app.description=args[++optind];
                    }
                else if(args[optind].equals("-t"))
                    {
                    app.type=args[++optind];
                    }
                else if(args[optind].equals("--"))
                    {
                    optind++;
                    break;
                    }
                else if(args[optind].startsWith("-"))
                    {
                    System.err.println("Unnown option: "+args[optind]);
                    return;
                    }
                else
                    {
                    break;
                    }
                ++optind;
                }

            app.run();
            } 
        catch (Exception e)
            {
            e.printStackTrace();
            }
        }
    }